# RAG Fundamentals

## What is RAG?
Retrieval-Augmented Generation combines an LLM with a knowledge retrieval system. Instead of relying solely on training data, the LLM retrieves relevant documents at inference time.

## RAG Pipeline
```
Query -> Embed Query -> Search Vector DB -> Retrieve Top-K Documents -> Augment Prompt -> LLM -> Response
```

## Why RAG?
- Access up-to-date information (beyond training cutoff)
- Ground responses in specific documents (reduce hallucination)
- No expensive fine-tuning needed
- Easy to update knowledge base
- Maintain data privacy (data stays in your DB)

## Components
1. **Document Loader**: Ingest PDFs, web pages, databases
2. **Text Splitter**: Chunk documents into manageable pieces
3. **Embedding Model**: Convert text to vectors
4. **Vector Store**: Store and search embeddings
5. **Retriever**: Find relevant chunks for a query
6. **LLM**: Generate response using retrieved context

## For Agentic AI
- RAG is THE primary way agents access knowledge
- Every enterprise agent uses RAG for domain-specific knowledge