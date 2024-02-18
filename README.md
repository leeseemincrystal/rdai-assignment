# Run application
Run the following command to run application on docker <br/>
docker build -t rdai . <br/>
docker run -d --name rdai -p 80:80 rdai <br/>

Check if application is running on http://127.0.0.1/docs <br/>
POST a request to /request, and you should get the response from the model <br/>

Example: <br/>

POST "Tell me about Large Language Models and how Quantization works" <br/>

<img width="1440" alt="Screenshot 2024-02-18 at 5 30 34 PM" src="https://github.com/leeseemincrystal/rdai-assignment/assets/50550784/d3a83963-574a-42e3-88c5-c31d725ca904">

Response body: <br/>
{
  "response": "\nLarge Language Models (LLMs) are models that can learn to generate human-like text by analyzing large amounts of text data. They are trained on large datasets that contain examples of human-generated text, such as textual reviews or text in social media. The models use neural networks to learn the patterns and structure of human language, which helps them generate new text that is similar in style and content to human-generated text.\n\nQuantization is a technique used to reduce the size of neural networks without compromising their accuracy. It is a process of compressing the weights and parameters of the neural network into a smaller size without losing any information about the original network. This process is achieved by converting the weights and parameters into a sequence of bits, known as a quantized vector.\n\nIn the context of LLMs, quantization is used to reduce the size of the LLM's parameters without compromising its ability to learn and generate human-like text. This is achieved by breaking down the LLM's parameters into a set of quantized vectors, which can then be represented as a sequence of bits. The number of bits used to represent each quantized vector depends on the complexity of the LLM's parameters."
}

<img width="1438" alt="Screenshot 2024-02-18 at 5 31 53 PM" src="https://github.com/leeseemincrystal/rdai-assignment/assets/50550784/68a7d159-37e1-4457-a50a-bc7c643fd638">
