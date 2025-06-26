# 🫁 Pneumonia Detection API

A machine learning-powered REST API built with FastAPI and TensorFlow for detecting pneumonia from chest X-ray images. This application uses a deep learning model trained on chest X-ray images to classify them as either normal or showing signs of pneumonia.

## 🚀 Features

- **Fast Image Classification**: Quickly analyze chest X-ray images for pneumonia detection
- **RESTful API**: Easy-to-use endpoints for image upload and prediction
- **High Accuracy**: Powered by a trained convolutional neural network
- **Confidence Scoring**: Returns prediction confidence percentages
- **Docker Support**: Containerized for easy deployment
- **Real-time Processing**: Instant results for uploaded images

## 🛠️ Tech Stack

- **Framework**: FastAPI
- **Machine Learning**: TensorFlow/Keras
- **Image Processing**: PIL (Pillow)
- **Server**: Uvicorn
- **Language**: Python 3.8+

## 📋 Prerequisites

- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

## ⚡ Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/isheunesutembo/pneumonia-detection-api.git
cd pneumonia-detection-api
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

The API will be available at `http://localhost:3000`

## 📦 Installation

### Using pip

```bash
pip install fastapi tensorflow pillow uvicorn python-multipart
```

### Using Docker

```bash
docker build -t pneumonia-detection .
docker run -p 3000:3000 pneumonia-detection
```

## 🔧 API Usage

### Upload and Analyze Image

**Endpoint**: `POST /predict`

**Request**:
```bash
curl -X POST "http://localhost:3000/predict" \
     -H "accept: application/json" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@chest_xray.jpg"
```

**Response**:
```json
{
  "prediction": "PNEUMONIA",
  "scoreconfidence": 87.45
}
```

### Health Check

**Endpoint**: `GET /health`

**Response**:
```json
{
  "status": "healthy",
  "model_loaded": true
}
```

## 📁 Project Structure

```
pneumonia-detection-api/
├── app.py                 # Main FastAPI application
├── model/
│   └── pneumonia_model.h5 # Trained TensorFlow model
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── .gitignore           # Git ignore file
├── README.md            # Project documentation
└── tests/
    ├── test_api.py      # API tests
    └── sample_images/   # Test images
```

## 🧠 Model Information

- **Architecture**: Convolutional Neural Network (CNN)(DenseNet121)
- **Input Size**: 224x224 pixels
- **Classes**: NORMAL, PNEUMONIA
- **Training Data**: Chest X-ray images dataset
- **Image Format**: Supports JPEG, PNG, and other common formats

## 🔍 Classification Details

The model processes images through the following steps:

1. **Preprocessing**: Resize to 224x224 and normalize pixel values
2. **Prediction**: Forward pass through the CNN
3. **Classification**: Threshold at 0.5 for binary classification
4. **Confidence**: Returns percentage confidence for the prediction

## 🐳 Docker Deployment

### Build Image

```bash
docker build -t pneumonia-detection .
```

### Run Container

```bash
docker run -d -p 3000:3000 --name pneumonia-api pneumonia-detection
```

### Docker Compose

```yaml
version: '3.8'
services:
  pneumonia-api:
    build: .
    ports:
      - "3000:3000"
    environment:
      - PORT=3000
```

## 🧪 Testing

Run the test suite:

```bash
pytest tests/
```

Test the API with sample images:

```bash
python test_prediction.py
```

## 📊 Performance

- **Accuracy**: ~88% on test dataset
- **Inference Time**: < 100ms per image
- **Supported Formats**: JPEG, PNG, TIFF
- **Max Image Size**: 10MB

## ⚠️ Important Notes

- This application is for **educational/research purposes only**
- **Not intended for medical diagnosis** - always consult healthcare professionals
- Ensure proper data privacy when handling medical images
- Model performance may vary with different image qualities and sources

## 🔒 Security Considerations

- Implement proper authentication for production use
- Add rate limiting to prevent abuse
- Validate and sanitize all file uploads
- Use HTTPS in production environments

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/isheunesutembo/pneumonia-detection-api/issues)
- **Documentation**: [API Docs](http://localhost:3000/docs) (when running locally)
- **Email**: isheunesu48@gmail.com

## 🙏 Acknowledgments

- Chest X-ray dataset providers
- TensorFlow and FastAPI communities
- Medical imaging research community

## 📈 Roadmap

- [ ] Add multi-class classification (different types of pneumonia)
- [ ] Implement batch processing
- [ ] Add model versioning
- [ ] Create web interface
- [ ] Add detailed logging and monitoring
- [ ] Implement A/B testing for model improvements

---

**⚠️ Medical Disclaimer**: This tool is not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of qualified health providers with questions about medical conditions.
