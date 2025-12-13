"use strict";
(function(){
  const inputId = 'search';
  function renderResults(query){
    const container = document.getElementById('results');
    container.innerHTML = '';
    const q = (query||'').toLowerCase();
    const list = [];
    for (const [k,v] of Object.entries(window.tipos_python||{})){
      if (k.includes(q) || v.term.includes(q) || (v.code||'').toLowerCase().includes(q)){
        list.push({title: v.term, code: v.code});
      }
    }
    (window.pitfalls||[]).forEach(p => { if ((p||'').toLowerCase().includes(q)) list.push({pitfall: p}); });
    (window.exemplos||[]).forEach(e => { if ((e||'').toLowerCase().includes(q)) list.push({example: e}); });
    list.forEach(item => {
      const card = document.createElement('div'); card.className = 'card result-card';
      if (item.title) { const h = document.createElement('h4'); h.textContent = item.title; card.appendChild(h); }
      if (item.code) { const pre = document.createElement('pre'); pre.className='example'; pre.textContent = item.code; card.appendChild(pre); }
      if (item.pitfall) { const pre = document.createElement('pre'); pre.className='pitfall'; pre.textContent = item.pitfall; card.appendChild(pre); }
      if (item.example) { const pre = document.createElement('pre'); pre.className='example'; pre.textContent = item.example; card.appendChild(pre); }
      container.appendChild(card);
    });
  }
  document.addEventListener('DOMContentLoaded', function(){
    const input = document.getElementById(inputId);
    if (input){
      input.addEventListener('input', (e)=> renderResults(e.target.value));
      renderResults('');
    }
  });
})();
