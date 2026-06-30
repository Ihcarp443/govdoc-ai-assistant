'use client';

import { useState } from 'react';

export default function ChatBot() {
  const [messages, setMessages] = useState([
    {
      id: 1,
      role: 'assistant',
      content: 'Hello! How can I help you today?'
    }
  ]);
  const [input, setInput] = useState('');
  const [isTyping, setIsTyping] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userMessage = {
      id: messages.length + 1,
      role: 'user',
      content: input.trim()
    };

    setMessages([...messages, userMessage]);
    setInput('');
    setIsTyping(true);

    setTimeout(() => {
      const assistantMessage = {
        id: messages.length + 2,
        role: 'assistant',
        content: 'This is a simulated response. In a real application, this would connect to an AI backend.'
      };
      setMessages(prev => [...prev, assistantMessage]);
      setIsTyping(false);
    }, 1500);
  };

  return (
    <div className="flex flex-col h-screen max-w-3xl mx-auto bg-white">
      {/* Header */}
      <div className="p-5 border-b border-gray-200 text-center bg-white">
        <h1 className="text-2xl font-semibold text-gray-900">ChatGPT</h1>
      </div>

      {/* Messages Container */}
      <div className="flex-1 overflow-y-auto p-5 flex flex-col gap-5">
        {messages.map((message) => (
          <div
            key={message.id}
            className={`flex gap-4 p-4 rounded-lg max-w-full ${
              message.role === 'user'
                ? 'bg-gray-50 flex-row-reverse'
                : 'bg-white'
            }`}
          >
            {/* Avatar */}
            <div
              className={`w-9 h-9 rounded flex items-center justify-center font-semibold text-sm flex-shrink-0 ${
                message.role === 'user'
                  ? 'bg-purple-600 text-white'
                  : 'bg-emerald-600 text-white'
              }`}
            >
              {message.role === 'user' ? 'U' : 'AI'}
            </div>

            {/* Message Content */}
            <div className="flex-1 min-w-0">
              <div className="font-semibold text-sm mb-1 text-gray-900">
                {message.role === 'user' ? 'You' : 'ChatGPT'}
              </div>
              <div className="text-base leading-relaxed text-gray-900 break-words">
                {message.content}
              </div>
            </div>
          </div>
        ))}

        {/* Typing Indicator */}
        {isTyping && (
          <div className="flex gap-4 p-4 rounded-lg bg-white">
            <div className="w-9 h-9 rounded bg-emerald-600 text-white flex items-center justify-center font-semibold text-sm flex-shrink-0">
              AI
            </div>
            <div className="flex-1">
              <div className="font-semibold text-sm mb-1 text-gray-900">ChatGPT</div>
              <div className="flex gap-1 py-2">
                <span className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '0s' }}></span>
                <span className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '0.2s' }}></span>
                <span className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '0.4s' }}></span>
              </div>
            </div>
          </div>
        )}
      </div>

      {/* Input Container */}
      <form onSubmit={handleSubmit} className="p-5 border-t border-gray-200 bg-white">
        <div className="flex items-end gap-3 bg-white border border-gray-300 rounded-xl px-4 py-3 shadow-sm focus-within:border-emerald-600 transition-colors">
          <textarea
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Send a message..."
            rows={1}
            className="flex-1 border-none outline-none resize-none text-base leading-6 max-h-48 bg-transparent text-gray-900 placeholder-gray-400"
            onKeyDown={(e) => {
              if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                handleSubmit(e);
              }
            }}
          />
          <button
            type="submit"
            disabled={!input.trim() || isTyping}
            className="w-8 h-8 border-none bg-emerald-600 text-white rounded-md cursor-pointer flex items-center justify-center transition-colors flex-shrink-0 hover:bg-emerald-700 disabled:bg-gray-300 disabled:cursor-not-allowed disabled:opacity-50"
          >
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" className="w-4 h-4">
              <path d="M22 2L11 13" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
              <path d="M22 2L15 22L11 13L2 9L22 2Z" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
            </svg>
          </button>
        </div>
      </form>
    </div>
  );
}