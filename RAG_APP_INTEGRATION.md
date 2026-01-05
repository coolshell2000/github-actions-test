# RAG求职应用集成说明

## 概述

RAG求职应用已作为子项目集成到github-actions-test主应用中。用户可以通过新的路由访问RAG系统的完整功能。

## 集成功能

### 1. 主应用增强
- 添加了 `/rag` 路由作为RAG应用的入口点
- 在访客历史页面添加了到RAG应用的链接
- 保持了统一的用户认证系统

### 2. RAG应用功能
- **职位搜索**：通过 `/rag/jobs` 访问
- **地图视图**：通过 `/rag/map` 访问
- **职位搜索**：通过 `/rag/search` 访问
- **用户认证**：与主应用共享登录状态

### 3. 目录结构
```
github-actions-test/
├── app/
│   └── main.py          # 主应用文件（已增强）
├── rag_app/             # RAG应用子项目
│   ├── app.py           # RAG应用主文件
│   ├── auth.py          # RAG应用认证模块
│   ├── config.py        # RAG应用配置模块
│   ├── database.py      # RAG应用数据库模块
│   ├── rag.py           # RAG应用核心模块
│   ├── job_collector.py # RAG应用职位收集器
│   ├── scraper.py       # RAG应用爬虫模块
│   └── main.py          # RAG应用主模块
├── rag_app.py           # RAG应用入口文件（副本）
└── ...
```

## 访问方式

- **RAG应用主页**：`https://github-actions-test-u5cx.onrender.com/rag`
- **职位列表**：`https://github-actions-test-u5cx.onrender.com/rag/jobs`
- **地图视图**：`https://github-actions-test-u5cx.onrender.com/rag/map`
- **职位搜索**：`https://github-actions-test-u5cx.onrender.com/rag/search`

## 用户体验

- 已登录用户可以直接访问RAG应用的全部功能
- 未登录用户需要先登录才能使用RAG应用的完整功能
- 所有访问都会被记录在访客历史中
- 保持了统一的用户界面风格

## 技术实现

- 使用Flask的路由系统集成两个应用
- 共享用户认证状态（Flask-Login）
- 共享数据库连接（SQLite）
- 保持了各自应用的独立性

## 配置要求

- 需要在环境变量中配置RAG应用所需的所有密钥
- 数据库路径需要正确配置以支持两个应用
- OAuth提供商配置保持不变

## 维护说明

- RAG应用的更新可以在`rag_app/`目录中独立进行
- 主应用的路由和集成代码在`app/main.py`中
- 两个应用共享相同的部署环境和依赖
