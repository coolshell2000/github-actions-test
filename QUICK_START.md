# 快速启动指南

## 环境准备

1. 确保已安装 Python 3.9+
2. 安装项目依赖：
   ```bash
   pip install -r requirements.txt
   ```

## 配置社交登录

项目已预配置Google OAuth密钥，可直接使用。

如需配置微信OAuth，请在 `.env` 文件中添加：
```
WECHAT_CLIENT_ID=your-wechat-client-id
WECHAT_CLIENT_SECRET=your-wechat-client-secret
```

## 启动应用

```bash
./start.sh
```

或手动启动：

```bash
cd app
python main.py
```

## 访问应用

- 主页: http://localhost:5000
- 登录页面: http://localhost:5000/login
- API状态: http://localhost:5000/api/status
- 用户资料: http://localhost:5000/profile (需登录)

## 功能测试

1. 访问 http://localhost:5000/login
2. 选择任一登录方式
3. 完成认证后查看用户资料页面

