---
title: Simple_Crackme_By_Antoni
---

{% raw %}{% capture solution %}
{% include_relative solution.txt %}
{% endcapture %}

## 📝 Solution

{{ solution | markdownify }}

{% raw %}
{% if site.static_files | where: "path", "/_challenges/Simple_Crackme_by_antoni/keygen.py" %}
## 🔑 Keygen (Python)

```py
{% include_relative keygen.py %}
{% endif %}{% endraw %}{% endraw %}
