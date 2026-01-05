# 社交登录功能说明

## 概述

本项目已成功集成社交登录功能，支持用户通过Google和微信进行登录。

## 功能特性

- 支持Google OAuth登录
- 支持微信OAuth登录
- 统一的用户管理系统
- 安全的认证流程
- 响应式登录页面

## 配置要求

### 环境变量

在使用社交登录功能前，需要在`.env`文件中配置以下环境变量：

```bash
# 必需的密钥
SECRET_KEY=your-secret-key-here

# Google OAuth配置（可选）
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret

# 微信OAuth配置（可选）
WECHAT_CLIENT_ID=your-wechat-client-id
WECHAT_CLIENT_SECRET=your-wechat-client-secret
```

### 依赖项

项目已包含所有必需的依赖：

- Flask-Login
- Authlib
- requests-oauthlib

## API端点

- `/login` - 显示登录选项页面
- `/login/google` - 重定向到Google登录
- `/login/wechat` - 重定向到微信登录
- `/callback/google` - Google OAuth回调
- `/callback/wechat` - 微信OAuth回调
- `/profile` - 用户资料页面（需要登录）
- `/logout` - 退出登录

## 数据库结构

用户表（users）包含以下字段：

- `id` - 用户唯一标识
- `email` - 用户邮箱（可选）
- `name` - 用户姓名
- `profile_pic` - 头像URL
- `created_at` - 创建时间
- `provider` - 登录提供商（google, wechat, local）
- `provider_user_id` - 提供商的用户ID

## 使用方法

1. 配置环境变量
2. 启动应用
3. 访问 `/login` 页面
4. 选择任一社交登录方式
5. 完成认证后，用户将被重定向到主页

## 安全考虑

- 所有OAuth流程都遵循标准协议
- 使用HTTPS重定向URL
- 实现了适当的错误处理
- 用户数据安全存储

## 部署说明

当部署到生产环境时：

1. 确保设置了强密钥（SECRET_KEY）
2. 配置正确的OAuth重定向URL
3. 使用HTTPS协议
4. 定期更新依赖包

## 故障排除

如果社交登录无法工作：

1. 检查环境变量是否正确设置
2. 确认OAuth应用已在提供商处正确配置
3. 检查重定向URL是否匹配
4. 查看应用日志以获取详细错误信息
