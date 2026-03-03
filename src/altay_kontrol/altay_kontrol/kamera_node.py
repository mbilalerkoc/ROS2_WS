import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from ultralytics import YOLO
import cv2

class KameraNode(Node):
    def __init__(self):
        super().__init__('kamera_node')
        self.publisher_ = self.create_publisher(String, '/tespit_verileri', 10)
        
        self.model = YOLO('/home/muhammetbilal/Desktop/goruntu-isleme-iha/models/best_yeni.pt') 
        self.cap = cv2.VideoCapture('/home/muhammetbilal/Desktop/goruntu-isleme-iha/videos/asfalt_kare.mp4')
        
        self.create_timer(0.1, self.isleme_callback) 

    def isleme_callback(self):
        success, frame = self.cap.read()
        if success:

            results = self.model(frame, conf=0.6, verbose=False)
            
            for r in results:
                for box in r.boxes:
                    x, y, w, h = box.xywh[0].tolist()
                    label = "HEDEF_KARE" 
                    
                    msg = String()
                    msg.data = f'{label}|{x:.1f}|{y:.1f}'
                    self.publisher_.publish(msg)
                    self.get_logger().info(f'Tespit: {msg.data}')

            cv2.imshow("KAPSUL-ALTAY Takip", results[0].plot())
            cv2.waitKey(1)
        else:
            self.get_logger().info('Video tamamlandı.')
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0) 

def main(args=None):
    rclpy.init(args=args)
    node = KameraNode()
    rclpy.spin(node)
    node.cap.release()
    cv2.destroyAllWindows()
    rclpy.shutdown()