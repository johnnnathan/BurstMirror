---
title: Crackme1_By_Majorsopa
---

{% raw %}{% capture solution %}
{% include_relative solution.txt %}
{% endcapture %}

## 📝 Solution

{{ solution | markdownify }}

{% raw %}
{% if site.static_files | where: "path", "/_challenges/crackme1_by_majorsopa/keygen.py" %}
## 🔑 Keygen (Python)

```py
{% include_relative keygen.py %}
{% endif %}{% endraw %}{% endraw %}
