---
title: Crackme 1_By_Para
---

{% raw %}{% capture solution %}
{% include_relative solution.txt %}
{% endcapture %}

## 📝 Solution

{{ solution | markdownify }}

{% raw %}
{% if site.static_files | where: "path", "/_challenges/crackme-1_by_para/keygen.py" %}
## 🔑 Keygen (Python)

```py
{% include_relative keygen.py %}
{% endif %}{% endraw %}{% endraw %}
