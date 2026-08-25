---
title: "BasketEvent: Understanding Who Did What and When in Basketball Videos"
collection: publications
permalink: /publication/2026-07-21-basketevent
date: 2026-08-01
paperurl: 'https://arxiv.org/abs/2607.21267'
---
<div class="research-item">
  <div class="research-figure">
    <img src="/images/research/basketevent.png" alt="BasketEvent teaser">
  </div>
  <div class="research-copy">
    <p>
    <strong>BasketEvent: Understanding Who Did What and When in Basketball Videos</strong><br>
    <a href="https://github.com/zhangyu2003" target="_blank">Yu Zhang</a>, <strong>Jiayuan Rao</strong>, <a href="https://haoningwu3639.github.io/" target="_blank">Haoning Wu</a>, <a href="https://weidixie.github.io/" target="_blank">Weidi Xie</a><br>
    <em>In BMVC 2026</em> <span style="color: red;"><strong>(New)</strong></span><br>
    [<a href="https://arxiv.org/abs/2607.21267" target="_blank">Paper</a>] / [<a href="https://zhangyu2003.github.io/BasketEvent/" target="_blank">Webpage</a>] / [<a href="https://huggingface.co/datasets/zaywas/BasketEvent" target="_blank">Dataset</a>] / [<a href="https://www.xiaohongshu.com/discovery/item/6a7b2a3400000000080127d5?source=webshare&xhsshare=pc_web&xsec_token=ABh07XV6wOe_5R8TBg21qJC9QUwXwvUpyS0wPuy4ABCKs=&xsec_source=pc_share" target="_blank">Demo</a>]
    </p>
  </div>
</div>

Comprehensive basketball video understanding requires resolving not only *what* event occurs, but also *who* is responsible and *when* the key evidence appears. However, existing methods typically treat spatial perception and semantic recognition as isolated tasks, failing to ground events to individual players or pinpoint their temporal boundaries within complex collective dynamics. To bridge this gap, we introduce **BasketEvent**, a player-centric basketball event understanding dataset curated from real NBA broadcasts. In BasketEvent, event labels are grounded to the responsible players, and a manually annotated subset of 1,000 samples with precise event intervals is provided to evaluate temporal evidence localization.

Based on this data, we propose **PlayNet**, a player-centric reasoning framework that maps basketball videos to player-level event predictions with temporal evidence. Concretely, PlayNet tracks key entities, associates player identities, and reasons about events by modeling player-player, player-ball, and global court interactions, while aggregating sparse temporal evidence via gated pooling. Extensive experiments demonstrate that PlayNet significantly outperforms representative video-level and crop-based baselines, proving the superiority of player-centric modeling for fine-grained sports video understanding. Our data, code, and models will be made publicly available.
