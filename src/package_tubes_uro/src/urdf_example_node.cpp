#include "rclcpp/rclcpp.hpp"
#include "urdf/model.h"

class URDFExampleNode : public rclcpp::Node
{
public:
  URDFExampleNode() : Node("urdf_example_node")
  {
    // Load URDF from file or string
    urdf::Model model;
    if (model.initFile("/path/to/your/robot.urdf"))
    {
      RCLCPP_INFO(this->get_logger(), "URDF loaded successfully!");
    }
    else
    {
      RCLCPP_ERROR(this->get_logger(), "Failed to load URDF.");
    }
  }
};

int main(int argc, char *argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<URDFExampleNode>());
  rclcpp::shutdown();
  return 0;
}
