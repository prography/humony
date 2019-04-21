import axios from 'axios';

const API_URL = 'http://localhost:8000/api';

export function sendImage (formData: any) {
    return axios.post(`${API_URL}/inpic/`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
    });
};
