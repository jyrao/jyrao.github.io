---
title: "WorldCupArena: Fine-Grained Evaluation of Language Models and Deep-Research Agents on Football Forecasting"
collection: preprints
permalink: /publication/2026-07-20-worldcuparena
date: 2026-07-20
paperurl: 'https://arxiv.org/abs/2607.18084'
---
<div class="research-item">
  <div class="research-figure">
    <img src="/images/research/worldcuparena-teaser.png" alt="WorldCupArena teaser">
  </div>
  <div class="research-copy">
    <p>
    <strong>WorldCupArena: Fine-Grained Evaluation of Language Models and Deep-Research Agents on Football Forecasting</strong><br>
    <a href="https://www.wzk.plus/" target="_blank">Zhaokai Wang</a>, Tianlin Gui, <strong>Jiayuan Rao</strong>, <a href="https://dszdsz.cn/" target="_blank">Shangzhe Di</a>, Yihong Tang, Dingli Liang<br>
    <em>In submission</em> <span style="color: red;"><strong>(New)</strong></span><br>
    [<a href="https://arxiv.org/abs/2607.18084" target="_blank">Paper</a>] / [<a href="https://www.matchmate.tv/predict/" target="_blank">Webpage</a>] / [<a href="https://github.com/wzk1015/WorldCupArena" target="_blank">Code</a>]
    </p>
  </div>
</div>

Predicting a football match before kickoff requires more than knowing past results: a model must use changing information and make a clear prediction before the answer is available. We present WorldCupArena, a dynamic benchmark for language models and deep-research agents. The 2026 FIFA World Cup is its first evaluation, and the same process can be reused for future leagues and cups. Before each match, a model either receives a common evidence package or searches for information itself. It predicts the result and score, likely players and events, match statistics, and the outcome of the competition. After the match, these predictions are compared with the recorded result.

We report result accuracy, exact-score accuracy, and a scoreline score that gives some credit when a predicted score is close but not exact, together with scores for the other prediction tasks. Across 104 matches and 13 systems, models with similar result accuracy differ more clearly on detailed predictions. Compared with betting-market and human-fan baselines, the best system shows only small gains in result and exact-score accuracy, but a clearer gain in Scoreline. New schedules can be added as they begin, allowing the benchmark to evaluate future models without using outcomes that are already known. Code, prompts, predictions, and evaluation scripts are open sourced at <a href="https://github.com/wzk1015/WorldCupArena" target="_blank">GitHub</a>.
