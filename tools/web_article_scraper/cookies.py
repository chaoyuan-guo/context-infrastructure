"""Circle.so Cookie 管理：加载、过期检查。"""

import json
import os
from datetime import datetime, timezone

COOKIE_PATH = os.path.expanduser("~/.config/circle-so/cookies.json")


def load_cookies(domain: str) -> tuple[list[dict] | None, str | None]:
    """从本地配置文件读取 Circle.so Cookie。

    Returns:
        (cookies_list, error_message)
        成功时 error_message 为 None；失败时 cookies_list 为 None。
    """
    if not os.path.exists(COOKIE_PATH):
        return None, f"Cookie 文件不存在: {COOKIE_PATH}，需要用户提供 Cookie"

    with open(COOKIE_PATH) as f:
        data = json.load(f)

    # 过期检查
    expires_at = data.get("expires_at", "")
    if expires_at:
        exp_date = datetime.strptime(expires_at, "%Y-%m-%d").replace(
            tzinfo=timezone.utc
        )
        remaining = (exp_date - datetime.now(timezone.utc)).days
        if remaining <= 0:
            return None, f"Cookie 已过期（{expires_at}），请用户重新提供"
        if remaining <= 30:
            print(f"⚠️  Cookie 将在 {remaining} 天后过期（{expires_at}），建议尽快更新")

    cookies = []
    for name, value in data.get("cookies", {}).items():
        cookies.append({"name": name, "value": value, "domain": domain, "path": "/"})

    return cookies, None
