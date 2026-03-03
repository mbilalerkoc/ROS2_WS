import rclpy
from rclpy.node import Node

class AltayNode(Node):
    def __init__(self):
        super().__init__('altay_node')
        self.get_logger().info('ROS 2 Sistemi Başlatıldı!')
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info('Dron verisi okunuyor...')

def main(args=None):
    rclpy.init(args=args)
    node = AltayNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()