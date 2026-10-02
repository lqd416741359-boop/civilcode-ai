<div align="center">

![CivilCode AI 封面](assets/cover.png)

# CivilCode AI

**中国大陆民法典研究与民事争议准备 Skill**

![License](https://img.shields.io/badge/license-MIT-c9a45b)
![Scope](https://img.shields.io/badge/scope-中国大陆民事法律-8b2f2f)
![Language](https://img.shields.io/badge/language-中文-123d35)
![Status](https://img.shields.io/badge/status-v1.0-2f855a)

</div>

## 项目简介

CivilCode AI 用于协助用户梳理中国大陆民事纠纷：建立当事人关系和时间线、识别涉及的民法典编章、核验现行法律与司法解释、分析可能的请求和抗辩、规划证据，并在条件充分时估算金额和准备行动方案。

它以《中华人民共和国民法典》为分析中心，但不会把民法典当作唯一依据；涉及程序、个人信息、消费者权益、公司事务或其他专门领域时，需要继续核验相关现行法律规则。

## 覆盖范围

- 总则：民事主体、民事行为、代理、时效和一般责任
- 物权：房产、登记、共有、相邻关系、担保物权和占有
- 合同：买卖、借款、租赁、服务、担保、违约和准合同
- 人格权：姓名、肖像、名誉、隐私和个人信息
- 婚姻家庭：婚姻、离婚、财产、债务、子女和家庭关系
- 继承：遗产、遗嘱、法定继承、遗赠和遗产债务
- 侵权责任：人身财产损害、网络、产品、交通、医疗、动物和建筑物等责任

## 使用示例

```text
请使用 $civilcode-ai 帮我分析：朋友向我借款20万元，只有转账记录和微信聊天，
约定去年还款但一直未还。我需要补充哪些事实和证据，可以提出哪些请求？
```

Skill 会先补齐足以改变结论的关键事实，再检索和核验现行规则。涉及具体法条、诉讼时效、司法解释、地方规则或金额时，应以分析当日的官方来源为准。

## 设计原则

- 先整理事实、关系和时间线，再作结论
- 同时扫描请求、抗辩、反请求和程序障碍
- 优先使用全国人大、国家法律法规数据库、最高人民法院和中国政府网等官方来源
- 不捏造法条、案号、司法解释或裁判结果
- 区分法律上的权利与证据上的可证明性
- 只读取与当前问题相关的参考文件，减少 Token 消耗
- 默认在聊天中回答，仅在用户明确要求时导出 Word 或 PDF

## 安装

将整个 `civilcode-ai` 文件夹复制到 Codex 的 Skills 目录，保持目录结构不变，然后重新加载或重启 Codex。

```text
civilcode-ai/
├── agents/openai.yaml
├── assets/
│   ├── cover.png
│   ├── social-preview.png
│   └── report-template.md
├── references/
├── scripts/civil_calculator.py
├── .gitignore
├── GITHUB_UPLOAD.md
├── LICENSE
├── README.md
└── SKILL.md
```

> 不同版本或安装方式的 Skills 路径可能不同，请以当前 Codex 版本的官方说明为准。

## 金额计算脚本

`scripts/civil_calculator.py` 只负责十进制金额、简单利息、比例分配和按份拆分等算术操作。它不会判断某项请求是否成立，也不会选择合法利率或责任比例。

## 重要声明

本项目仅用于一般性法律信息研究、事实整理和案件准备，不构成法律意见，不建立律师—客户关系，也不能代替持证律师或有关机构针对具体事实提供的帮助。法律和司法解释可能更新，具体案件还可能受到证据、程序、地域、时间效力及其他专门法律的影响。

## GitHub 发布

仓库名称、简介、Topics、Social Preview 和逐步上传方法集中写在 [GITHUB_UPLOAD.md](GITHUB_UPLOAD.md)。

## License

本项目采用 [MIT License](LICENSE)。封面图为本仓库配套制作，可随项目在 MIT License 条款下使用。
