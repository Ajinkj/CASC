# Customer Assistance Smart Cart (CASC)

The **Customer Assistance Smart Cart** (CASC) is an intelligent, autonomous cart designed to enhance the shopping experience in supermarkets by assisting customers in locating and collecting their desired products. CASC aims to address common shopping challenges, such as difficulty finding products and limited staff availability, by navigating to product locations and guiding customers efficiently.

## Project Overview

The Smart Cart will:
1. **Interact with Customers**: Detect and engage with customers automatically.
2. **Guide to Desired Products**: Respond to customer requests by navigating to the specific product locations.
3. **Follow the Customer's Pace**: Move at a pace matching the customer, tracking them throughout the journey.
4. **Navigate with Barcode Scanning**: Recognize junctions and directions by scanning barcodes placed at each junction.
5. **Provide Product Positioning**: Once at the destination, instruct the customer on the exact location of the product on the shelf.

## Example Use Case

1. A customer asks the Smart Cart for "rice."
2. The Smart Cart guides the customer to the rice section.
3. The customer places the rice packet in the cart.
4. The Smart Cart waits for the next item request or moves to the next requested location.

## Features

- **Automatic Customer Detection**: Initiates interaction as soon as a customer is detected.
- **Product Navigation**: Finds the shortest path to the requested product using barcode-guided navigation.
- **Pace Matching**: Adjusts speed to match the customer's walking pace.
- **Line Following**: Uses line-following sensors to stay on track.
- **Location Feedback**: Provides instructions about the product's position on the shelf.

## Components

### Hardware

1. **Raspberry Pi / Arduino** (1 unit) - Main controller for processing inputs and controlling navigation.
2. **IoT Module** (1 unit) - Allows connectivity for potential network or cloud integration.
3. **Camera Module** (2 units) - Used for customer detection and barcode scanning.
4. **Barcode Scanner** (1 unit) - Scans barcodes at junctions for navigation guidance.
5. **LCD Display (16x2)** (1 unit) - Displays navigation and interaction messages.
6. **Microphone Module** (1 unit) - For voice command input from the customer.
7. **Speaker Module** (1 unit) - Provides audio feedback to the customer.
8. **Servo Motors** (4 units) - Controls wheel movement and direction.
9. **Motor Driver Unit** (1 unit) - Drives the motors with appropriate power.
10. **IR Sensors** (2 units) - Assists in line following.
11. **Ultrasonic Sensors** (2 units) - Detects obstacles and adjusts path if needed.
12. **Battery (12V)** (1 unit) - Powers the entire cart.
13. **Body Frame** (1 unit) - Physical frame to hold all components.

### Additional Components for Line Following

- **Arduino Uno**
- **L293D Motor Driver** - For controlling motor speed and direction.
- **BO Motor** - Provides wheel motion.
- **Wheels**
- **Lithium-ion Battery**
- **Jumper Cables** - For connecting components.

## Working Principle

The **line follower robot** acts as a foundation for the CASC. It navigates based on a visual line, typically a black line on a white surface, using IR sensors to detect the line and follow it accurately. CASC expands on this concept by integrating barcode scanning at each junction to determine directions, enabling it to follow complex paths in a supermarket.

## How It Works

1. **Initiate Interaction**: CASC detects a customer and starts an interaction.
2. **Product Request**: The customer asks CASC for a product.
3. **Barcode Navigation**: CASC scans barcodes at each junction to follow the correct path.
4. **Arrive at Destination**: Upon reaching the desired product location, CASC provides instructions about the product's position on the shelf.
5. **Product Collection**: The customer picks the product and places it in the cart.
6. **Next Request**: CASC awaits the next product request or guides the customer to checkout.

## Future Enhancements

- **Inventory Management**: CASC could potentially update inventory in real-time as items are picked.
- **Voice Recognition**: Improved speech recognition for more natural interactions.
- **Data Analytics**: Integration with cloud-based analytics to monitor shopping patterns.

## Conclusion

The **Customer Assistance Smart Cart (CASC)** revolutionizes the shopping experience by combining robotics, IoT, and AI to create an intelligent assistant for navigating supermarkets. With its ability to detect customers, guide them to products, and provide a seamless shopping experience, CASC is a step towards the future of retail.
