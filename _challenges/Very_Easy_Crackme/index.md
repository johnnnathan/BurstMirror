---
title: Very_Easy_Crackme 
---

{% capture solution %}
{% include_relative solution.txt %}
{% endcapture %}

## 📝 Solution

{{ solution | markdownify }}

{% if site.static_files | where: "path", "/_challenges/Very_Easy_Crackme/keygen.py" %}
## 🔑 Keygen (Python)

```py
{% include_relative keygen.py %}
```
{% endif %}

