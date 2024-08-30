## RAG

大模型 RAG 相关的模型，开源框架等开发资源。

### 开源框架
|名称|Stars|简介|备注|
|---|---|---|---|
|[LlamaIndex](https://github.com/jerryjliu/llama_index) | ![GitHub Repo stars](https://img.shields.io/github/stars/jerryjliu/llama_index.svg?style=social) | Provides a central interface to connect your LLMs with external data. |将llm与外部数据连接起来。|
|[QAnything](https://github.com/netease-youdao/QAnything)|![GitHub Repo stars](https://badgen.net/github/stars/netease-youdao/QAnything)|Question and Answer based on Anything.|QAnything (Question and Answer based on Anything) 是致力于支持任意格式文件或数据库的本地知识库问答系统，可断网安装使用。您的任何格式的本地文件都可以往里扔，即可获得准确、快速、靠谱的问答体验。目前已支持格式: PDF(pdf)，Word(docx)，PPT(pptx)，XLS(xlsx)，Markdown(md)，电子邮件(eml)，TXT(txt)，图片(jpg，jpeg，png)，CSV(csv)，网页链接(html)|
|[ragflow](https://github.com/infiniflow/ragflow)|![GitHub Repo stars](https://badgen.net/github/stars/infiniflow/ragflow)|RAGFlow is an open-source RAG (Retrieval-Augmented Generation) engine based on deep document understanding.|RAGFlow 是一款基于深度文档理解构建的开源 RAG（Retrieval-Augmented Generation）引擎。RAGFlow 可以为各种规模的企业及个人提供一套精简的 RAG 工作流程，结合大语言模型（LLM）针对用户各类不同的复杂格式数据提供可靠的问答以及有理有据的引用。|
|[FastGPT](https://github.com/labring/FastGPT)|![GitHub Repo stars](https://badgen.net/github/stars/labring/FastGPT)|FastGPT is a knowledge-based platform built on the LLMs, offers a comprehensive suite of out-of-the-box capabilities such as data processing, RAG retrieval, and visual AI workflow orchestration, letting you easily develop and deploy complex question-answering systems without the need for extensive setup or configuration.|FastGPT 是一个基于 LLM 大语言模型的知识库问答系统，提供开箱即用的数据处理、模型调用等能力。同时可以通过 Flow 可视化进行工作流编排，从而实现复杂的问答场景！|
|[langchain](https://github.com/hwchase17/langchain)|![GitHub Repo stars](https://badgen.net/github/stars/hwchase17/langchain)|Building applications with LLMs through composability|开发自己的 ChatGPT 应用|
|[graphrag](https://github.com/microsoft/graphrag)|![GitHub Repo stars](https://badgen.net/github/stars/microsoft/graphrag)|A modular graph-based Retrieval-Augmented Generation (RAG) system |基于知识图谱的检索增强生成（RAG）系统|
|[kotaemon](https://github.com/Cinnamon/kotaemon)|![GitHub Repo stars](https://badgen.net/github/stars/Cinnamon/kotaemon)|An open-source RAG-based tool for chatting with your documents.|基于开源 RAG 的工具，用于与您的文档聊天。|



### Embedding 模型和 Reranker 模型

|名称|Stars|简介|备注|
|---|---|---|---|
|[FlagEmbedding](https://github.com/FlagOpen/FlagEmbedding)|![GitHub Repo stars](https://badgen.net/github/stars/FlagOpen/FlagEmbedding)|Retrieval and Retrieval-augmented LLMs.|中文使用量排名前列的模型。BGE Embedding是一个通用向量模型。 使用retromae 对模型进行预训练，再用对比学习在大规模成对数据上训练模型。|
|[BCEmbedding](https://github.com/netease-youdao/BCEmbedding) | ![GitHub Repo stars](https://img.shields.io/github/stars/netease-youdao/BCEmbedding) | Netease Youdao's open-source embedding and reranker models for RAG products. |BCEmbedding是由网易有道开发的中英双语和跨语种语义表征算法模型库，其中包含 EmbeddingModel和 RerankerModel两类基础模型。EmbeddingModel专门用于生成语义向量，在语义搜索和问答中起着关键作用，而 RerankerModel擅长优化语义搜索结果和语义相关顺序精排。|
|[jina-embeddings-v2-base-en](https://huggingface.co/jinaai/jina-embeddings-v2-base-en)|-|jina-embeddings-v2-base-en is an English, monolingual embedding model supporting 8192 sequence length. It is based on a BERT architecture (JinaBERT) that supports the symmetric bidirectional variant of ALiBi to allow longer sequence length.|jina-embeddings-v2-base-en 是一个英文单语言嵌入模型，支持序列长度为 8192。它基于 JinaBERT 架构，支持 ALiBi 的对称双向变体，以允许更长的序列长度。主干 jina-bert-v2-base-en 在 C4 数据集上预训练。该模型进一步在 Jina AI 的超过 4 亿对句子和硬负样本的集合上进行训练。这些对来自各种领域，并通过彻底的清理过程精心挑选。|
