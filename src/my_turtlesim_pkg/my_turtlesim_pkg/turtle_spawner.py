import rclpy 
from rclpy.node import Node 
from turtlesim.srv import Spawn
from functools import partial 
import random
import math 
from my_turtlesim_interfaces.msg import Turtle 
from my_turtlesim_interfaces.msg import TurtleArray
from my_turtlesim_interfaces.srv import CatchTurtle
from turtlesim.srv import Kill



class TurtleSpawnerNode(Node):
    def __init__(self):
        super().__init__("turtle_spawner")

        self.declare_parameter("turtle_name_prefix", "myturtle")
        self.declare_parameter("spawn_frequency", 1.25)


        self.turtle_name_prefix = self.get_parameter("turtle_name_prefix").value
        self.frequency_ = self.get_parameter("spawn_frequency").value


        self.turtle_number = 0 
        self.turtles_alive_ = []
        self.alive_turtles_publisher_ = self.create_publisher(TurtleArray, "alive_turtles", 10)
        self.spawn_client_ = self.create_client(Spawn, "/spawn")
        self.catch_turtle_service_ = self.create_service(CatchTurtle, "catch_turtle", self.catch_turtle)
        self.kill_client_ = self.create_client(Kill, "/kill")
        self.spawn_turtle_timer_ = self.create_timer(1.0/self.frequency_ , self.spawn_new_turtle)

    def catch_turtle(self, request:CatchTurtle.Request, response:CatchTurtle.Response):
        #call Kill service 
        self.call_kill_service(request.name)
        response.success = True 
        return response 
    
    def publish_alive_turtles(self):
        msg = TurtleArray()
        msg.turtles = self.turtles_alive_
        self.alive_turtles_publisher_.publish(msg)


    def spawn_new_turtle(self):
        self.turtle_number += 1
        name = self.turtle_name_prefix + str(self.turtle_number)
        x = random.uniform(0.0, 11.0)
        y = random.uniform(0.0,11.0)
        theta = random.uniform (0.0, 2*math.pi)
        self.call_spawn_service(name, x, y, theta)

    def call_spawn_service(self, turtle_name, x, y, theta):
        while not self.spawn_client_.wait_for_service(1.0):
            self.get_logger().warn("Waiting for Spawn Service.....")

        request = Spawn.Request()
        request.x = x
        request.y = y
        request.theta = theta
        request.name = turtle_name

        future = self.spawn_client_.call_async(request)
        future.add_done_callback(partial(self.callback_call_spawn_service, request=request))


    def callback_call_spawn_service(self, future, request: Spawn.Request):
        response = future.result()

        if response.name != "":
            self.get_logger().info("New Alive Turtle : " + response.name)   
            new_turtle = Turtle()
            new_turtle.name = response.name 
            new_turtle.x =  request.x
            new_turtle.y  = request.y 
            new_turtle.theta = request.theta
            self.turtles_alive_.append(new_turtle)
            self.publish_alive_turtles()     

    def call_kill_service(self, turtle_name):
        while not self.kill_client_.wait_for_service(1.0):
            self.get_logger().warn("Waiting for Kill Service....")

        request = Kill.Request()
        request.name = turtle_name

        future = self.kill_client_.call_async(request)
        future.add_done_callback(partial(self.callback_call_kill_service, turtle_name=turtle_name))

    def callback_call_kill_service(self, future, turtle_name):
        for (i, turtle) in enumerate(self.turtles_alive_):
            if turtle.name == turtle_name:
                del self.turtles_alive_[i]
                self.publish_alive_turtles()
                break



def main(args=None):
    rclpy.init(args=args)
    node = TurtleSpawnerNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()