---
title: "Multi-Agent System for Comprehensive Soccer Understanding"
collection: preprints
permalink: /publication/2025-05-06-soccceragent
date: 2025-05-06
paperurl: 'https://jyrao.github.io/SoccerAgent/'
---
<div style="display: flex; align-items: center;"> <!-- 添加align-items: center; 来垂直居中所有子元素 -->
  <div style="flex: 1; width: 25%; text-align: center; margin-right: 5%;"> <!-- text-align: center; 用于水平居中图片 -->
    <img src="https://jyrao.github.io/SoccerAgent/static/images/agent.png" style="width: 100%; max-width: 100%; height: auto;" alt="描述">
  </div>
  <div style="flex: 3; width: 75%;">
    <p>
    <strong>Multi-Agent System for Comprehensive Soccer Understanding</strong><br>
    <strong>Jiayuan Rao*</strong>, <a href="https://openreview.net/profile?id=~Zifeng_Li3" target="_blank">Zifeng Li*</a>, <a href="https://haoningwu3639.github.io/" target="_blank">Haoning Wu</a>, <a href="https://mediabrain.sjtu.edu.cn/yazhang/" target="_blank">Ya Zhang</a>, <a href="https://cmic.sjtu.edu.cn/wangyanfeng/" target="_blank">Yanfeng Wang</a>, <a href="https://weidixie.github.io/" target="_blank">Weidi Xie</a><br>
    <em>In Submission</em> <span style="color: red;">(New)</span><br>
    [<a href="https://arxiv.org/abs/2505.03735" target="_blank">Paper</a>] / [<a href="https://jyrao.github.io/SoccerAgent/" target="_blank">Webpage</a>] / [<a href="https://github.com/jyrao/SoccerAgent" target="_blank">Code</a>] / [<a href="https://huggingface.co/" target="_blank">Dataset (soon)</a>]
    </p>
  </div>
</div>

Recent advancements in AI-driven soccer understanding have demonstrated rapid progress, yet existing research predominantly focuses on isolated or narrow tasks. To bridge this gap, we propose a comprehensive framework for holistic soccer understanding. Specifically, we make the following contributions in this paper: (i) we construct SoccerWiki, the first large-scale multimodal soccer knowledge base, integrating rich domain knowledge about players, teams, referees, and venues to enable knowledge-driven reasoning; (ii) we present SoccerBench, the largest and most comprehensive soccer-specific benchmark, featuring around 10K standardized multimodal (text, image, video) multi-choice QA pairs across 13 distinct understanding tasks, curated through automated pipelines and manual verification; (iii) we introduce SoccerAgent, a novel multi-agent system that decomposes complex soccer questions via collaborative reasoning, leveraging domain expertise from SoccerWiki and achieving robust performance; (iv) extensive evaluations and ablations that benchmark state-of-the-art MLLMs on SoccerBench, highlighting the superiority of our proposed agentic system.