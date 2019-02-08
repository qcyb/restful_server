import sys
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt


def Usage():
    print("""
    python ./{0} -hostname 127.0.0.1 -port 8080 -transport websockets -topic emqtt -qos 0 -payload 'Hello World' -client_id 'client_id2' -username user2 -password password
    """.format(__file__))


def init_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-hostname', metavar='<hostname>', type=str, dest='hostname')
    parser.add_argument('-transport', metavar='<transport>', type=str, dest='transport')
    parser.add_argument('-port', metavar='<port>', type=int, dest='port')
    parser.add_argument('-topic', metavar='<topic>', type=str, dest='topic')
    parser.add_argument('-qos', metavar='<qos>', type=int, dest='qos')
    parser.add_argument('-payload', metavar='<payload>', type=str, dest='payload')
    parser.add_argument('-client_id', metavar='<client_id>', type=str, dest='client_id')
    parser.add_argument('-username', metavar='<username>', type=str, dest='username')
    parser.add_argument('-password', metavar='<password>', type=str, dest='password')
    parser.print_help = Usage
    return parser.parse_args()


def main(args):
    headers = {
        "Host": args.hostname,
    }
    # 方法1(推荐):
    client = mqtt.Client(client_id=args.client_id, transport=args.transport)
    client.username_pw_set(username=args.username, password=args.password)
    # client.ws_set_options(path="/mqtt", headers=headers)
    client.connect(args.hostname, args.port, 60)
    client.publish(topic=args.topic, payload=args.payload, qos=args.qos)

    # 方法2:
    # auth = {'username': args.username, 'password': args.password}
    # publish.single(
    #     args.topic, payload=args.payload, qos=args.qos, hostname=args.hostname,
    #     port=args.port, args.client_id=args.client_id, auth=auth,
    #     transport=args.transport
    # )


if __name__=="__main__":
    if len(sys.argv) == 1:
        Usage(), sys.exit()
    args = init_args()
    main(args)
