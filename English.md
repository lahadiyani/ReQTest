## ReQTest

ReQTest is a Python-based tool for sending HTTP requests to a target server and performing a UDP flood attack. It provides a simple command-line interface for users to specify the target URL, number of requests, maximum delay, victim IP address, target port, and flood attack duration.

### Requirements

To use ReQTest, make sure you have the following requirements installed:

- Python 3.x
- Requests library: You can install it using pip with the following command:
  ```
  pip install requests
  ```
- Colorama library: You can install it using pip with the following command:
  ```
  pip install colorama
  ```

### Usage

1. Clone the repository or download the "ReQTest.py" file to your local machine.

2. Open a terminal or command prompt and navigate to the directory where the "ReQTest.py" file is located.

3. Run the following command to start the ReQTest tool:
   ```
   python ReQTest.py
   ```

4. Follow the prompts in the command-line interface to provide the necessary inputs:
   - Enter the target URL.
   - Enter the number of requests to be sent.
   - Enter the maximum delay in seconds between requests.
   - Enter the victim's IP address.
   - Enter the target port.
   - Enter the duration of the UDP flood attack in seconds.

5. ReQTest will send the specified number of HTTP requests to the target server and display the response status codes, response times, and site health status for each request. It will also perform a UDP flood attack on the specified victim IP address and port.

6. After the requests are sent and the flood attack is completed, a file named "hasil.txt" will be created in the same directory. This file will contain information about the target URL, victim IP, response status codes, response times, and site health status for each request.

### Disclaimer

Please note that ReQTest is a tool for educational purposes only. It should only be used on websites and servers that you have permission to test. Using ReQTest for any malicious or unauthorized activities is strictly prohibited. The developers of ReQTest are not responsible for any misuse or damage caused by the tool.

### Conclusion

ReQTest is a handy tool for sending HTTP requests and performing UDP flood attacks. By following the provided documentation and using the tool responsibly, you can gain insights into server response times and test the resilience of your own systems against flood attacks.

If you have any questions or need further assistance, please don't hesitate to contact the developers of ReQTest.

Happy testing!

---
