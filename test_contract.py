import pytest
from contract import NewsVerificationContract

def test_verify_news_claim():
    contract = NewsVerificationContract()
    result = contract.verify_news_claim(
        article_id="test-1",
        claim_text="Web3 adoption is increasing globally.",
        source_url="https://example.com/news"
    )
    
    assert result["is_verified"] is True
    assert result["trust_score"] == 85
    assert "test-1" in contract.verified_articles

def test_get_article_status():
    contract = NewsVerificationContract()
    contract.verify_news_claim(
        article_id="test-2",
        claim_text="Blockchain AI integration.",
        source_url="https://example.com/ai"
    )
    status = contract.get_article_status("test-2")
    assert status["trust_score"] == 85
    
    missing = contract.get_article_status("non-existent")
    assert missing["is_verified"] is False
