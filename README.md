# 📱 Telegram API Hash & ID Tool 🚀

Welcome to **ReZNuM's Telegram API Tool**! This Python script helps you retrieve your **Telegram API Hash** and **API ID** with ease. Perfect for developers building Telegram bots or apps! 🤖

---

## ✨ Features

- 🛡️ Securely fetches your Telegram API Hash and ID using the official Telegram website.
- 🎨 Beautiful terminal interface with colorful ASCII art and an unscramble effect for contact info.
- 🔒 Handles authentication with phone number and verification code.
- 📋 Displays additional details like Public Key and Production Configuration.
- 🚫 Gracefully handles errors like rate limits or invalid inputs.

---

## 🛠️ Requirements

To run this tool, you'll need the following Python libraries:

- `requests` 📡
- `beautifulsoup4` 🕸️
- `colorama` 🌈
- `time` ⏳
- `random` 🎲
- `sys` ⚙️

Install them using pip:

```bash
pip install requests beautifulsoup4 colorama
```

---

## 🚀 How to Use

1. **Clone the repository** 📥:

   ```bash
   git clone https://github.com/ItsReZNuM/Telegram-API-Tool.git
   cd Telegram-API-Tool
   ```

2. **Run the script** 🏃‍♂️:

   ```bash
   python ApiHash.py
   ```

3. **Follow the prompts** 📲:

   - Enter your phone number with the country code (e.g., `+98XXXXXX`).
   - Enter the verification code sent to your Telegram account.

4. **Get your APIs** 🎉:

   The tool will display your **API ID**, **API Hash**, **Public Key**, and **Production Configuration** if successful. If there's an error, it will let you know with a friendly message. 😊

---

## 📸 Screenshots

### Starting the Tool
![Tool Start](https://via.placeholder.com/600x200.png?text=Tool+Start+Screen)

### Successful API Retrieval
![API Success](https://via.placeholder.com/600x200.png?text=API+Success+Screen)

### Error Handling
![Error Screen](https://via.placeholder.com/600x200.png?text=Error+Screen)

---

## 🐛 Known Issues

- Some accounts may face rate-limiting issues. If you see "Too many tries," wait 8 hours before retrying. ⏰
- In rare cases, the API retrieval might fail due to changes in Telegram's website structure. Stay tuned for updates! 🔧

---

## 📬 Contact Me

Feel free to reach out for support or suggestions! 😄

- **Telegram**: [@ItsReZNuM](https://t.me/ItsReZNuM) 📱
- **Instagram**: [ReZ.NuM](https://instagram.com/ReZ.NuM) 📷
- **GitHub**: [ItsReZNuM](https://github.com/ItsReZNuM) 🖥️

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve the tool, please:

1. Fork the repository 🍴
2. Create a new branch (`git checkout -b feature/awesome-feature`) 🌿
3. Commit your changes (`git commit -m 'Add awesome feature'`) 💾
4. Push to the branch (`git push origin feature/awesome-feature`) 🚀
5. Open a Pull Request 📬

---

## 🌟 Acknowledgments

- Thanks to the open-source community for the amazing libraries used in this project! 🙌
- Inspired by the need for a simple Telegram API retrieval tool. 💡

Happy coding! 🎉