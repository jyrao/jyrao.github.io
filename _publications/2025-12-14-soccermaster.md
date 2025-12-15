---
title: "SoccerMaster: A Vision Foundation Model for Soccer Understanding"
collection: preprints
permalink: /publication/2025-12-14-soccermaster
date: 2025-12-14
paperurl: 'https://haolinyang-hlyang.github.io/SoccerMaster/'

---
<div style="display: flex; align-items: center;"> <!-- 添加align-items: center; 来垂直居中所有子元素 -->
  <div style="flex: 1; width: 25%; text-align: center; margin-right: 5%;"> <!-- text-align: center; 用于水平居中图片 -->
    <img src="https://haolinyang-hlyang.github.io/SoccerMaster/static/images/teaser.jpg" style="width: 100%; max-width: 100%; height: auto;" alt="描述">
  </div>
  <div style="flex: 3; width: 75%;">
    <p>
    <strong>SoccerMaster: A Vision Foundation Model for Soccer Understanding</strong><br>
    <a href="https://haolinyang-hlyang.github.io/" target="_blank"> Haolin Yang</a>, <strong>Jiayuan Rao</strong>, <a href="https://haoningwu3639.github.io/" target="_blank">Haoning Wu</a>, <a href="https://weidixie.github.io/" target="_blank">Weidi Xie</a><br>
    <em>Technical Report</em> <span style="color: red;">(New)</span><br>
    [<a href="https://arxiv.org/abs/2512.11016" target="_blank">Paper</a>] / [<a href="https://haolinyang-hlyang.github.io/SoccerMaster/" target="_blank">Webpage</a>] / [<a href="https://github.com/haolinyang-hlyang/SoccerMaster" target="_blank">Code</a>] / [<a href="https://huggingface.co" target="_blank">Dataset (soon)</a>]
    </p>
  </div>
</div>

Soccer understanding has recently garnered growing research interest due to its domain-specific complexity and unique challenges. Unlike prior works that typically rely on isolated, task-specific expert models, this work aims to propose a unified model to handle diverse soccer visual understanding tasks, ranging from fine-grained perception (e.g., athlete detection) to semantic reasoning (e.g., event classification). Specifically, our contributions are threefold: (i) we present SoccerMaster, the first soccer-specific vision foundation model that unifies diverse understanding tasks within a single framework via supervised multi-task pretraining; (ii) we develop an automated data curation pipeline to generate scalable spatial annotations, and integrate them with various existing soccer video datasets to construct SoccerFactory, a comprehensive pretraining data resource; and (iii) we conduct extensive evaluations demonstrating that SoccerMaster consistently outperforms task-specific expert models across diverse downstream tasks, highlighting its breadth and superiority. The data, code, and model will be publicly available.