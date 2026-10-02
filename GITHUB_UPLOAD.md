# GitHub 上传设置

上传仓库文件时，请上传 `civilcode-ai` 文件夹内的全部内容，包括 `.gitignore`；不要把外面的 ZIP 上传进仓库。

## 新建仓库

- **Repository name：** `civilcode-ai`
- **Description：** `中国大陆民法典研究与民事争议准备 Skill：梳理关系与时间线、核验法律依据、规划证据并分析请求和抗辩。`
- **Visibility：** `Public`
- **Add a README file：** 不勾选
- **Add .gitignore：** 选择 `None`
- **Choose a license：** 选择 `None`

本文件夹已经包含 README、忽略文件和 MIT License，不需要 GitHub 再次生成。

## 上传文件

1. 创建仓库后选择 **Add file → Upload files**。
2. 打开本地 `civilcode-ai` 文件夹并全选其中全部内容，不要上传外层文件夹。
3. 确认上传列表中包含 `agents`、`assets`、`references`、`scripts`、`SKILL.md`、`README.md`、`LICENSE`、`.gitignore` 和本文件。
4. Commit message 填写：`Initial release of CivilCode AI`
5. 点击 **Commit changes**。

## About 简介与 Topics

在仓库首页右侧 **About** 区域点击齿轮：

- **Description：** `中国大陆民法典研究与民事争议准备 Skill：梳理关系与时间线、核验法律依据、规划证据并分析请求和抗辩。`
- **Website：** 留空

加入以下 Topics：

```text
codex-skill
ai-skill
civil-code
civil-law
legal-research
china
prc
legal-ai
```

## Social Preview 封面

README 顶部会自动显示 `assets/cover.png`。如需分享仓库链接时显示专用封面：

1. 打开仓库 **Settings → General**。
2. 找到 **Social preview**。
3. 上传 `assets/social-preview.png` 并保存。

## 推荐版本

- 首个 Release 标签：`v1.0.0`
- Release 标题：`CivilCode AI v1.0.0`
- Release 简介：`首个公开版本：支持中国大陆民事纠纷关系梳理、民法典七编路由、现行法律研究、证据规划、请求与抗辩分析及金额估算。`

第一次上传时不必立即创建 Release，可以在仓库文件确认无误后再创建。

## 上传后检查

- README 顶部封面正常显示且中文无乱码
- `SKILL.md` 位于仓库根目录
- `agents/openai.yaml` 存在
- 两张封面均能打开
- GitHub 识别为 MIT License
- 仓库中没有 ZIP、临时文件或重复嵌套的 `civilcode-ai/civilcode-ai` 目录
