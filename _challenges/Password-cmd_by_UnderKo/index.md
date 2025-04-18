---
title: Password Cmd_By_Underko
---

{% capture solution %}
{% include_relative solution.txt %}
{% endcapture %}

## 📝 Solution

{{ solution | markdownify }}

{% assign file = site.static_files | where: "path", "/_challenges/Password-cmd_by_UnderKo/keygen.py" | first %}
## 🔑 Keygen (Python)

```py
{% include_relative keygen.py %}
```
