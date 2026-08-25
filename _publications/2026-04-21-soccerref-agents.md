---
title: "SoccerRef-Agents: Multi-Agent System for Automated Soccer Refereeing"
collection: publications
permalink: /publication/2026-04-21-soccerref-agents
date: 2025-12-13
paperurl: 'https://arxiv.org/abs/2604.23392'
---
<div class="research-item">
  <div class="research-figure">
    <img src="/images/research/soccerref-agents.png" alt="SoccerRef-Agents teaser">
  </div>
  <div class="research-copy">
    <p>
    <strong>SoccerRef-Agents: Multi-Agent System for Automated Soccer Refereeing</strong><br>
    Zi Meng, Wanli Song, Yi Hu, <strong>Jiayuan Rao</strong>, Gang Chen<br>
    <em>In ISACE 2026</em> <span style="color: red;"><strong>(Oral)</strong></span><br>
    [<a href="https://arxiv.org/abs/2604.23392" target="_blank">Paper</a>]
    </p>
  </div>
</div>

Refereeing is vital in sports, where fair, accurate, and explainable decisions are fundamental. While intelligent assistant technologies are being widely adopted in soccer refereeing, current AI-assisted approaches remain preliminary. Existing research mostly focuses on isolated video perception tasks and lacks the ability to understand and reason about foul scenarios. To fill this gap, we propose SoccerRef-Agents, a holistic and explainable multi-agent decision-making framework for soccer refereeing.

The main contributions are: (i) constructing the multimodal benchmark SoccerRefBench with over 1,200 referee theory questions and 600 foul video clips; (ii) building a vector-based knowledge base RefKnowledgeDB using the latest "Laws of the Game" and a classic case database for precise, knowledge-driven reasoning; and (iii) designing a novel multi-agent architecture that collaborates via cross-modal RAG to bridge the semantic gap between visual content and regulatory texts. This work explores the technical capability of integrating MLLMs with refereeing expertise, and evaluations show our system significantly outperforms general-purpose MLLMs in decision accuracy and explanation quality. All databases, benchmarks, and code will be made available.
