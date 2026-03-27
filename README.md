# Daily Papers
The project automatically fetches the latest papers from arXiv based on keywords.

The subheadings in the README file represent the search keywords.

Only the most recent articles for each keyword are retained, up to a maximum of 100 papers.

You can click the 'Watch' button to receive daily email notifications.

## Getting Started
To track your own keywords, fork this repository and modify the `config.yaml` file. The GitHub Action is configured to run daily, fetching new papers and updating this README automatically. You can also trigger the workflow manually under the "Actions" tab.

Last update: 2026-03-27

## RAG
| **Title** | **Date** | **Abstract** | **Comment** |
| --- | --- | --- | --- |
| **[Retrieval Improvements Do Not Guarantee Better Answers: A Study of RAG for AI Policy QA](https://arxiv.org/abs/2603.24580v1)** | 2026-03-25 | <details><summary>Show</summary><p>Retrieval-augmented generation (RAG) systems are increasingly used to analyze complex policy documents, but achieving sufficient reliability for expert usage remains challenging in domains characterized by dense legal language and evolving, overlapping regulatory frameworks. We study the application of RAG to AI governance and policy analysis using the AI Governance and Regulatory Archive (AGORA) corpus, a curated collection of 947 AI policy documents. Our system combines a ColBERT-based retriever fine-tuned with contrastive learning and a generator aligned to human preferences using Direct Preference Optimization (DPO). We construct synthetic queries and collect pairwise preferences to adapt the system to the policy domain. Through experiments evaluating retrieval quality, answer relevance, and faithfulness, we find that domain-specific fine-tuning improves retrieval metrics but does not consistently improve end-to-end question answering performance. In some cases, stronger retrieval counterintuitively leads to more confident hallucinations when relevant documents are absent from the corpus. These results highlight a key concern for those building policy-focused RAG systems: improvements to individual components do not necessarily translate to more reliable answers. Our findings provide practical insights for designing grounded question-answering systems over dynamic regulatory corpora.</p></details> |  |
| **[Who Benefits from RAG? The Role of Exposure, Utility and Attribution Bias](https://arxiv.org/abs/2603.24218v1)** | 2026-03-25 | <details><summary>Show</summary><p>Large Language Models (LLMs) enhanced with Retrieval-Augmented Generation (RAG) have achieved substantial improvements in accuracy by grounding their responses in external documents that are relevant to the user's query. However, relatively little work has investigated the impact of RAG in terms of fairness. Particularly, it is not yet known if queries that are associated with certain groups within a fairness category systematically receive higher accuracy, or accuracy improvements in RAG systems compared to LLM-only, a phenomenon we refer to as query group fairness. In this work, we conduct extensive experiments to investigate the impact of three key factors on query group fairness in RAG, namely: Group exposure, i.e., the proportion of documents from each group appe