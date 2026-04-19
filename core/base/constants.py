"""
constants.py - 插件使用的常量
"""

# 注入到 System Prompt 的记忆头尾格式
MEMORY_INJECTION_HEADER = "<RAG-Faiss-Memory>"
MEMORY_INJECTION_FOOTER = "</RAG-Faiss-Memory>"

# 伪造工具调用注入相关常量（上游 2.2.6 新增）
FAKE_TOOL_CALL_NAME = "recall_long_term_memory"  # 复用已注册的工具名
FAKE_TOOL_CALL_ID_PREFIX = "fake_recall_"  # ID 前缀，用于清理时识别伪造消息

# 记忆类型对应的衰减倍率（相对于基础 decay_rate）
MEMORY_TYPE_DECAY_MULTIPLIERS = {
    "fact": 0.3,        # 事实：衰减很慢
    "preference": 0.5,  # 偏好：衰减较慢
    "event": 1.5,       # 事件：衰减适中
    "intent": 3.0,      # 意图：衰减最快
}
