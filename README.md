# jable-mcp

基于 MCP 协议的 jable.tv 番号视频下载服务。

## 功能
- 通过 MCP API、命令行工具实现根据番号下载 jable.tv 视频。
- 支持 Docker 部署。
- 参考 https://github.com/hcjohn463/JableTVDownload 下载实现。

## 用法
- Docker 方式：参考 Dockerfile 一键运行。
- Python 方式：pip install -r requirements.txt，运行 src/mcp_server.py。