---
title: SimpleCrackmeEzDiaoL 
---

{% capture solution %}
{% include_relative solution.txt %}
{% endcapture %}

## 📝 Solution

{{ solution | markdownify }}

{% assign file = site.static_files | where: "path", "/_challenges/SimpleCrackmeEzDiaoL/keygen.py" | first %}
## 🔑 Keygen (Python)

```c
{% include_relative keygen.c%}
```
