---
layout: default
title: Crackmes
---

# 🔐 Crackme Challenges

{% for item in site.challenges %}
- [{{ item.title }}]({{ item.url }})
{% endfor %}
