const API_BASE_URL = 'http://localhost:8000';

export const chatService = {
  async sendMessage(userId, content) {
    try {
      const response = await fetch(`${API_BASE_URL}/chat/${userId}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ content })
      });
      
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      
      return await response.json();
    } catch (error) {
      console.error('Error:', error);
      throw error;
    }
  },

  async clearHistory(userId) {
    try {
      const response = await fetch(`${API_BASE_URL}/chat/${userId}`, {
        method: 'DELETE'
      });
      
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      
      return await response.json();
    } catch (error) {
      console.error('Error:', error);
      throw error;
    }
  }
};