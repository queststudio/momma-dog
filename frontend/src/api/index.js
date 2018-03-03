import axios from 'axios';
import config from '../config';

const baseUrl = config.apiUrl;

const locks = {
  fetch: () => axios.get(`${baseUrl}/locks`).then(result => result.data.locks)
};

const switches = {
  fetch: () => axios.get(`${baseUrl}/switches`).then(result => result.data.switches),
  set: (id, state) => {
    const body = {
      state
    };
    const url = `${baseUrl}/switches/${id}`;
    return axios.put(url, body);
  }
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
  switches,
  locks,
  puzzles
};