<<<<<<< HEAD
# Hospital Virtual Assistant Chatbot 🏥

A medical chatbot application built with FastAPI and React that helps users with basic health queries and medical information. The chatbot provides general health guidance while maintaining appropriate medical disclaimers and ethical guidelines.

## Features 🚀

- Real-time chat interface
- Medical symptom assessment
- General health information
- Emergency guidance when necessary
- Professional medical disclaimers
- Responsive design
- Session persistence
- Medical guidance history

## Tech Stack 💻

### Backend
- Python 3.8+
- FastAPI
- OpenAI GPT-4
- uvicorn

### Frontend
- React
- Tailwind CSS
- lucide-react
- React Hooks

## Prerequisites 📋

Before running this project, make sure you have:

- Node.js (v14 or higher)
- Python 3.8 or higher
- OpenAI API key
- npm or yarn package manager

## Installation 🔧

### Backend Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/hospital-chatbot.git
cd hospital-chatbot
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install Python dependencies:
```bash
cd backend
pip install -r requirements.txt
```

4. Create a `.env` file in the backend directory:
```env
OPENAI_API_KEY=your_api_key_here
```

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

## Running the Application 🚀

### Start the Backend Server

```bash
cd backend
uvicorn main:app --reload --port 8000
```

### Start the Frontend Development Server

```bash
cd frontend
npm start
```

The application will be available at `http://localhost:3000`

## API Endpoints 📡

- `POST /chat/{user_id}`: Send a message to the chatbot
- `DELETE /chat/{user_id}`: Clear chat history
- `GET /health`: Health check endpoint

## Environment Variables 🔐

### Backend
- `OPENAI_API_KEY`: Your OpenAI API key

### Frontend
- No environment variables required for basic setup

## Project Structure 📁

```
hospital-chatbot/
├── backend/
│   ├── main.py
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   └── ChatInterface.jsx
│   │   ├── services/
│   │   │   └── api.js
│   │   ├── App.jsx
│   │   └── index.js
│   ├── package.json
│   └── tailwind.config.js
└── README.md
```

## Contributing 🤝

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License 📝

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer ⚠️

This chatbot is for informational purposes only and is not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.

## Acknowledgments 🙏

- OpenAI for providing the GPT API
- FastAPI team for the amazing framework
- React team for the frontend framework
- All contributors who help to improve this project

## Support 📧

For support, email: crispinni013@gmail.com or open an issue in the repository.

