import pytest
import requests
from config.config import Config


class TestTestmozAPI:
    """Test Testmoz website without browser using requests"""
    
    def test_testmoz_homepage_accessible(self):
        """Test that Testmoz homepage is accessible"""
        response = requests.get("https://testmoz.com/", timeout=10)
        assert response.status_code == 200
        assert "testmoz" in response.text.lower()
    
    def test_testmoz_homepage_content(self):
        """Test that Testmoz homepage contains expected content"""
        response = requests.get("https://testmoz.com/", timeout=10)
        content = response.text.lower()
        
        # Check for key content
        assert "easily create tests" in content
        assert "distribute your tests online" in content
        assert "build a test" in content
        assert "try a demo test" in content
    
    def test_testmoz_navigation_links(self):
        """Test that navigation links are present in HTML"""
        response = requests.get("https://testmoz.com/", timeout=10)
        content = response.text.lower()
        
        # Check for navigation links
        assert "features" in content
        assert "pricing" in content
        assert "faqs" in content
    
    def test_testmoz_features_section(self):
        """Test that features section is present"""
        response = requests.get("https://testmoz.com/", timeout=10)
        content = response.text.lower()
        
        # Check for features content
        assert "testmoz is" in content
        assert "simple" in content
        assert "teachers" in content
        assert "trainers" in content
        assert "employers" in content
    
    def test_testmoz_response_headers(self):
        """Test that response headers are correct"""
        response = requests.get("https://testmoz.com/", timeout=10)
        
        # Check important headers
        assert response.status_code == 200
        assert "text/html" in response.headers.get("content-type", "").lower()
        assert response.headers.get("server") is not None
    
    def test_testmoz_page_load_time(self):
        """Test that page loads within reasonable time"""
        import time
        start_time = time.time()
        response = requests.get("https://testmoz.com/", timeout=10)
        load_time = time.time() - start_time
        
        assert response.status_code == 200
        assert load_time < 5.0  # Should load within 5 seconds
    
    def test_testmoz_ssl_certificate(self):
        """Test that SSL certificate is valid"""
        response = requests.get("https://testmoz.com/", timeout=10, verify=True)
        assert response.status_code == 200
    
    def test_testmoz_redirects(self):
        """Test that redirects work correctly"""
        # Test with trailing slash
        response = requests.get("https://testmoz.com", timeout=10, allow_redirects=True)
        assert response.status_code == 200
        assert "testmoz.com" in response.url
    
    def test_testmoz_mobile_friendly(self):
        """Test that page is mobile-friendly (has viewport meta tag)"""
        response = requests.get("https://testmoz.com/", timeout=10)
        content = response.text.lower()
        
        # Check for mobile-friendly meta tags
        assert "viewport" in content or "mobile" in content
    
    def test_testmoz_seo_elements(self):
        """Test that page has basic SEO elements"""
        response = requests.get("https://testmoz.com/", timeout=10)
        content = response.text.lower()
        
        # Check for basic SEO elements
        assert "<title>" in content
        assert "<meta" in content
        assert "description" in content
