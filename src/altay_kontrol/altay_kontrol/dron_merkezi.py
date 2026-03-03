import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class DronMerkezi(Node):
    def __init__(self):
        super().__init__('dron_merkezi')

        self.publisher_ = self.create_publisher(String, '/dron_telemetri', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = f'İHA - İrtifa: {self.i} metre'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Yayınlanıyor: "{msg.data}"')
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    node = DronMerkezi()
    rclpy.spin(node)
    rclpy.shutdown()