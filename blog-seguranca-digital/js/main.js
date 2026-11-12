// ===== MENU MOBILE =====
document.addEventListener('DOMContentLoaded', () => {
  const menuToggle = document.querySelector('.menu-toggle');
  const mainNav = document.querySelector('.main-nav');

  if (menuToggle && mainNav) {
    menuToggle.addEventListener('click', () => {
      mainNav.classList.toggle('open');
      const expanded = mainNav.classList.contains('open');
      menuToggle.setAttribute('aria-expanded', expanded);
      menuToggle.textContent = expanded ? '✕' : '☰';
    });

    // Fecha menu ao clicar em um link
    mainNav.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        mainNav.classList.remove('open');
        menuToggle.setAttribute('aria-expanded', 'false');
        menuToggle.textContent = '☰';
      });
    });
  }

  // Marcar link ativo
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.main-nav a').forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPage || (currentPage === '' && href === 'index.html')) {
      link.classList.add('active');
    }
  });

  // Animação de entrada dos cards
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        setTimeout(() => {
          entry.target.classList.add('animate-in');
        }, i * 100);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('.post-card, .about-card, .transparency-card').forEach(el => {
    el.style.opacity = '0';
    observer.observe(el);
  });

  // Carregar posts dinâmicos na página inicial
  loadDynamicPosts();
});

// ===== SISTEMA DE POSTS DINÂMICOS =====
function getPosts() {
  const posts = localStorage.getItem('blogPosts');
  return posts ? JSON.parse(posts) : [];
}

function savePosts(posts) {
  localStorage.setItem('blogPosts', JSON.stringify(posts));
}

function createPost(title, category, content, author) {
  const posts = getPosts();
  const post = {
    id: Date.now(),
    title: title,
    category: category,
    content: content,
    author: author || 'Equipe CyberSeguro',
    date: new Date().toLocaleDateString('pt-BR'),
    excerpt: content.replace(/<[^>]*>/g, '').substring(0, 150) + '...'
  };
  posts.unshift(post);
  savePosts(posts);
  return post;
}

function deletePost(id) {
  if (!window.confirm('Tem certeza que deseja excluir esta postagem?')) return;

  let posts = getPosts();
  posts = posts.filter(p => p.id !== id);
  savePosts(posts);
  loadDynamicPosts();
  showNotification('Postagem excluída com sucesso.');
}

function loadDynamicPosts() {
  const grid = document.getElementById('dynamic-posts');
  if (!grid) return;

  const posts = getPosts();
  if (posts.length === 0) {
    grid.innerHTML = '';
    return;
  }

  const heading = document.createElement('h2');
  heading.className = 'section-title';
  heading.textContent = '📝 Publicações da Comunidade';
  heading.style.marginTop = '48px';

  const postsHTML = posts.map(post => `
    <article class="post-card dynamic-post-card">
      <div class="card-image" style="background: linear-gradient(135deg, #34a853 0%, #0d652d 100%); display:flex; align-items:center; justify-content:center;">
        <span style="font-size:3rem;">📝</span>
      </div>
      <div class="card-body">
        <h3>${escapeHTML(post.title)}</h3>
        <p class="card-excerpt">${escapeHTML(post.excerpt)}</p>
        <div class="card-footer">
          <span class="date">📅 ${post.date}</span>
          <div class="post-actions">
            <a href="#" class="read-more" onclick="viewPost(${post.id}); return false;">Ler mais</a>
            <button type="button" class="delete-post-button" onclick="deletePost(${post.id})" aria-label="Excluir postagem">Excluir</button>
          </div>
        </div>
      </div>
    </article>
  `).join('');

  grid.innerHTML = '';
  grid.appendChild(heading);

  const gridDiv = document.createElement('div');
  gridDiv.className = 'posts-grid';
  gridDiv.innerHTML = postsHTML;
  grid.appendChild(gridDiv);
}

function viewPost(id) {
  const posts = getPosts();
  const post = posts.find(p => p.id === id);
  if (!post) return;

  const win = window.open('', '_blank');
  win.document.write(`
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>${escapeHTML(post.title)} - CyberSeguro</title>
      <link rel="stylesheet" href="css/style.css">
    </head>
    <body>
      <header class="site-header">
        <div class="header-inner">
          <a href="index.html" class="site-logo">
            <span class="logo-icon">🛡️</span>
            <span>CyberSeguro</span>
          </a>
        </div>
      </header>
      <main class="main-content">
        <div class="article-container">
          <div class="article-header">
            <p class="breadcrumb"><a href="index.html">Início</a> / Publicação da Comunidade</p>
            <h1>${escapeHTML(post.title)}</h1>
            <div class="article-meta">
              <span>📅 ${post.date}</span>
              <span>✍️ ${escapeHTML(post.author)}</span>
              <span>📂 ${escapeHTML(post.category)}</span>
            </div>
          </div>
          <div class="article-content">
            ${post.content}
          </div>
        </div>
      </main>
    </body>
    </html>
  `);
  win.document.close();
}

function escapeHTML(str) {
  const div = document.createElement('div');
  div.textContent = str;
  return div.innerHTML;
}

// ===== FORMULÁRIO DE CONTATO =====
function handleContactForm(event) {
  event.preventDefault();
  const form = event.target;
  const name = form.querySelector('#name').value;
  const email = form.querySelector('#email').value;
  const message = form.querySelector('#message').value;

  if (!name || !email || !message) {
    showNotification('Por favor, preencha todos os campos.', 'error');
    return;
  }

  // Salvar mensagem no localStorage (simulação)
  const messages = JSON.parse(localStorage.getItem('contactMessages') || '[]');
  messages.push({ name, email, message, date: new Date().toLocaleDateString('pt-BR') });
  localStorage.setItem('contactMessages', JSON.stringify(messages));

  showNotification('Mensagem enviada com sucesso! Obrigado pelo contato. ✅');
  form.reset();
}

// ===== CRIAR POSTAGEM =====
function handleCreatePost(event) {
  event.preventDefault();
  const form = event.target;
  const title = form.querySelector('#post-title').value;
  const category = form.querySelector('#post-category').value;
  const author = form.querySelector('#post-author').value;
  const content = form.querySelector('#post-content').value;

  if (!title || !content) {
    showNotification('Título e conteúdo são obrigatórios!', 'error');
    return;
  }

  // Converter quebras de linha em parágrafos
  const formattedContent = content.split('\n\n').map(p => `<p>${p.replace(/\n/g, '<br>')}</p>`).join('');

  createPost(title, category, formattedContent, author);
  showNotification('Postagem publicada com sucesso! 🎉');
  form.reset();

  // Mostrar preview
  updatePreview(title, category, formattedContent, author);
}

function updatePreview(title, category, content, author) {
  const preview = document.getElementById('post-preview');
  if (!preview) return;

  preview.classList.add('active');
  preview.innerHTML = `
    <h2 style="margin-bottom:8px; color: var(--dark);">Pré-visualização</h2>
    <hr style="margin-bottom:24px; border-color: var(--gray-300);">
    <span style="background: var(--accent); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.75rem; font-weight: 600;">${escapeHTML(category)}</span>
    <h1 style="margin: 16px 0 8px; font-size: 1.8rem;">${escapeHTML(title)}</h1>
    <p style="color: var(--gray-500); font-size: 0.9rem; margin-bottom: 24px;">✍️ ${escapeHTML(author)} • 📅 ${new Date().toLocaleDateString('pt-BR')}</p>
    <div class="article-content" style="box-shadow:none; padding:0;">
      ${content}
    </div>
    <div style="margin-top: 24px; text-align: center;">
      <a href="index.html" class="btn-primary" style="text-decoration:none; color:white;">Ver no Blog</a>
    </div>
  `;
}

function livePreview() {
  const title = document.getElementById('post-title')?.value || '';
  const category = document.getElementById('post-category')?.value || '';
  const author = document.getElementById('post-author')?.value || 'Equipe CyberSeguro';
  const content = document.getElementById('post-content')?.value || '';

  if (title || content) {
    const formattedContent = content.split('\n\n').map(p => `<p>${p.replace(/\n/g, '<br>')}</p>`).join('');
    updatePreview(title, category, formattedContent, author);
  }
}

// ===== EDITOR TOOLBAR =====
function insertFormat(format) {
  const textarea = document.getElementById('post-content');
  if (!textarea) return;

  const start = textarea.selectionStart;
  const end = textarea.selectionEnd;
  const selected = textarea.value.substring(start, end);

  let insertion = '';
  switch (format) {
    case 'bold':
      insertion = `<strong>${selected || 'texto em negrito'}</strong>`;
      break;
    case 'italic':
      insertion = `<em>${selected || 'texto em itálico'}</em>`;
      break;
    case 'h2':
      insertion = `\n<h2>${selected || 'Subtítulo'}</h2>\n`;
      break;
    case 'h3':
      insertion = `\n<h3>${selected || 'Subtítulo menor'}</h3>\n`;
      break;
    case 'link':
      insertion = `<a href="https://">${selected || 'texto do link'}</a>`;
      break;
    case 'list':
      insertion = `\n<ul>\n  <li>${selected || 'Item 1'}</li>\n  <li>Item 2</li>\n  <li>Item 3</li>\n</ul>\n`;
      break;
    case 'quote':
      insertion = `\n<blockquote>${selected || 'Citação aqui'}</blockquote>\n`;
      break;
    case 'tip':
      insertion = `\n<div class="tip-box"><p class="tip-title">💡 Dica</p><p>${selected || 'Sua dica aqui'}</p></div>\n`;
      break;
    case 'warning':
      insertion = `\n<div class="warning-box"><p class="warning-title">⚠️ Atenção</p><p>${selected || 'Aviso importante'}</p></div>\n`;
      break;
  }

  textarea.value = textarea.value.substring(0, start) + insertion + textarea.value.substring(end);
  textarea.focus();
}

// ===== NOTIFICAÇÃO =====
function showNotification(message, type = 'success') {
  // Remove notificação anterior
  const existing = document.querySelector('.notification');
  if (existing) existing.remove();

  const notif = document.createElement('div');
  notif.className = `notification ${type}`;
  notif.textContent = message;
  document.body.appendChild(notif);

  requestAnimationFrame(() => {
    notif.classList.add('show');
  });

  setTimeout(() => {
    notif.classList.remove('show');
    setTimeout(() => notif.remove(), 400);
  }, 3500);
}
