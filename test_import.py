try:
    from langchain.chains import ConversationChain
    print("Module imported successfully!")
except ImportError as e:
    print(f"Import error: {e}")