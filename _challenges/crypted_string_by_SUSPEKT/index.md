---
title: Crypted_String_By_Suspekt
---

{% capture solution %}
{% include_relative solution.txt %}
{% endcapture %}

## 📝 Solution

{{ solution | markdownify }}

{% if site.static_files | where: "path", "/_challenges/crypted_string_by_SUSPEKT/keygen.py" %}
## 🔑 Keygen (Python)

```py
{% include_relative keygen.py %}
```
{% endif %}
