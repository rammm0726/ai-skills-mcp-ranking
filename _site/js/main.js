// Main JavaScript for AI Skills Ranking Website

(function() {
    'use strict';

    // Language switching
    const langButtons = document.querySelectorAll('.lang-btn');
    let currentLang = localStorage.getItem('lang') || 'zh';

    function setLanguage(lang) {
        currentLang = lang;
        localStorage.setItem('lang', lang);
        document.documentElement.lang = lang === 'zh' ? 'zh-CN' : 'en';

        // Update all i18n elements
        document.querySelectorAll('[data-i18n]').forEach(el => {
            const key = el.getAttribute('data-i18n');
            if (window.I18N && window.I18N[lang] && window.I18N[lang][key]) {
                el.textContent = window.I18N[lang][key];
            }
        });

        // Update placeholders
        document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
            const key = el.getAttribute('data-i18n-placeholder');
            if (window.I18N && window.I18N[lang] && window.I18N[lang][key]) {
                el.placeholder = window.I18N[lang][key];
            }
        });

        // Update language buttons
        langButtons.forEach(btn => {
            btn.classList.toggle('active', btn.dataset.lang === lang);
        });

        // Toggle nav text
        document.querySelectorAll('.nav-zh').forEach(el => {
            el.style.display = lang === 'zh' ? 'inline' : 'none';
        });
        document.querySelectorAll('.nav-en').forEach(el => {
            el.style.display = lang === 'en' ? 'inline' : 'none';
        });
    }

    // Language button click handlers
    langButtons.forEach(btn => {
        btn.addEventListener('click', function() {
            setLanguage(this.dataset.lang);
        });
    });

    // Back to top button
    const backToTopBtn = document.getElementById('back-to-top');
    if (backToTopBtn) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 300) {
                backToTopBtn.classList.add('visible');
            } else {
                backToTopBtn.classList.remove('visible');
            }
        });

        backToTopBtn.addEventListener('click', function() {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // Initialize on DOM ready
    document.addEventListener('DOMContentLoaded', function() {
        setLanguage(currentLang);
    });

    // Copy command functionality
    window.copyCommand = function(element) {
        const text = element.textContent;
        navigator.clipboard.writeText(text).then(function() {
            const btn = element.nextElementSibling;
            if (btn && btn.classList.contains('copy-btn')) {
                const originalText = btn.textContent;
                btn.textContent = currentLang === 'zh' ? '\u5df2\u590d\u5236!' : 'Copied!';
                btn.classList.add('copied');
                setTimeout(function() {
                    btn.textContent = originalText;
                    btn.classList.remove('copied');
                }, 2000);
            }
        }).catch(function() {
            // Fallback for older browsers
            const textarea = document.createElement('textarea');
            textarea.value = text;
            document.body.appendChild(textarea);
            textarea.select();
            document.execCommand('copy');
            document.body.removeChild(textarea);
        });
    };
})();
