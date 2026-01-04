# GitHub Actions Test Project

## 步骤1: 已在GitHub上创建仓库
✓ 仓库 github-actions-test 已创建

## 步骤2: 推送代码到GitHub
在终端中运行以下命令：
```
cd /mnt/nvme0n1p1/home/bt/Desktop/rag/VideoCode/使用Python构建RAG系统/rag/github-actions-test
git remote set-url origin git@github.com:coolshell2000/github-actions-test.git
git push -u origin main
```

## 步骤3: 观察GitHub Actions
- 推送后，GitHub Actions将自动运行
- 访问仓库的 Actions 标签页查看运行状态
- 您的Python脚本将在云端执行

## 项目结构
- `test_script.py` - 简单的Python脚本
- `.github/workflows/test-actions.yml` - GitHub Actions工作流配置
- 当您推送代码后，工作流将自动运行并执行Python脚本
