import axios from 'axios';

const baseUrl = 'http://localhost:8000/api';//todo make configurable 92.168.1.106

const locks = {
  fetch: () => axios.get(`${baseUrl}/locks`).then(result => result.data.locks)
};

const puzzles = {
  set: (reporter, address, state) => {
    const body = {
      state
    };
    const url = `${baseUrl}/reporters/${reporter}/puzzles/${address}`;
    return axios.put(url, body);
  }
};


export {
  locks,
  puzzles
};