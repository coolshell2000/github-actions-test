# 可部署Flask应用

这是一个可部署的Flask应用示例，展示了如何使用GitHub Actions进行持续集成和部署。

## 项目结构

- `app/main.py` - Flask应用主文件
- `requirements.txt` - Python依赖
- `Dockerfile` - Docker容器配置
- `Procfile` - 云平台部署配置
- `.github/workflows/` - GitHub Actions工作流

## 本地运行

1. 安装依赖：
   ```
   pip install -r requirements.txt
   ```

2. 运行应用：
   ```
   python app/main.py
   ```

3. 访问应用：
   - 主页: http://localhost:5000
   - API状态: http://localhost:5000/api/status
   - 健康检查: http://localhost:5000/health

## 部署选项

### Docker部署
```
docker build -t flask-app .
docker run -p 5000:5000 flask-app
```

### 云平台部署
应用已配置为可在以下平台部署：
- Heroku (通过Procfile)
- AWS Elastic Beanstalk
- Google Cloud Platform
- Microsoft Azure

## CI/CD

GitHub Actions将：
- 测试代码质量
- 运行单元测试
- 部署到生产环境（仅main分支）

## API端点

- `GET /` - 主页
- `GET /api/status` - API状态
- `GET /health` - 健康检查

