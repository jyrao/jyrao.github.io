---
title: "MatchTime: Towards Automatic Soccer Game Commentary Generation"
collection: publications
permalink: /publication/2024-06-16-matchtime
date: 2024-06-16
paperurl: 'https://haoningwu3639.github.io/MatchTime/'
---
<div style="display: flex; align-items: center;"> <!-- 添加align-items: center; 来垂直居中所有子元素 -->
  <div style="flex: 1; width: 25%; text-align: center; margin-right: 5%;"> <!-- text-align: center; 用于水平居中图片 -->
    <img src="https://github.com/jyrao/jyrao.github.io/blob/master/images/research/matchtime.png?raw=true" style="width: 100%; max-width: 100%; height: auto;" alt="描述">
  </div>
  <div style="flex: 3; width: 75%;">
    <p>
    <strong>MatchTime: Towards Automatic Soccer Game Commentary Generation</strong><br>
    <strong>Jiayuan Rao*</strong>, <a href="https://haoningwu3639.github.io/" target="_blank">Haoning Wu*</a>, <a href="https://verg-avesta.github.io/" target="_blank">Chang Liu</a>, <a href="https://cmic.sjtu.edu.cn/wangyanfeng/" target="_blank">Yanfeng Wang</a>, <a href="https://weidixie.github.io/" target="_blank">Weidi Xie</a><br>
    <em>In EMNLP 2024</em> <span style="color: red;">(Oral Presentation)</span><br>
    [<a href="https://arxiv.org/abs/2406.18530" target="_blank">Paper</a>]/ [<a href="https://haoningwu3639.github.io/MatchTime/" target="_blank">Webpage</a>] / [<a href="https://github.com/jyrao/MatchTime" target="_blank">Code</a>] / [<a href="https://www.bilibili.com/video/BV1L4421U76m" target="_blank">Demo</a>] / [<a href="https://mp.weixin.qq.com/s/BWe6-dox21oeqJcdy2DcpA?token=1469677986&lang=zh_CN" target="_blank">WeChat</a>]
    </p>
  </div>
</div>

Soccer is a globally popular sport with a vast audience, in this paper, we consider constructing an automatic soccer game commentary model to improve the audiences' viewing experience. In general, we make the following contributions: First, observing the prevalent video-text misalignment in existing datasets, we manually annotate timestamps for 49 matches, establishing a more robust benchmark for soccer game commentary generation, termed as SN-Caption-test-align; Second, we propose a multi-modal temporal alignment pipeline to automatically correct and filter the existing dataset at scale, creating a higher-quality soccer game commentary dataset for training, denoted as MatchTime; Third, based on our curated dataset, we train an automatic commentary generation model, named MatchVoice. Extensive experiments and ablation studies have demonstrated the effectiveness of our alignment pipeline, and training model on the curated datasets achieves state-of-the-art performance for commentary generation, showcasing that better alignment can lead to significant performance improvements in downstream tasks.

<!-- Jiayuan Rao*, Haoning Wu*, Chang Liu, Yanfeng Wang, Weidi Xie

[PDF](https://arxiv.org/pdf/2406.18530) / [arxiv]('https://arxiv.org/abs/2406.18530') / [Page](https://haoningwu3639.github.io/MatchTime/) -->
