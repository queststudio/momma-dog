import axios from 'axios';
import config from '../config';

const baseUrl = config.apiUrl;

const switchesArray = [
    {"id": 1, "label": "\u0417\u0430\u0432\u0438\u0441\u0442\u044c", "address": 56, "port": 5, "state": "off"},
    {"id": 2, "label": "\u041f\u043e\u0445\u043e\u0442\u044c", "address": 56, "port": 6, "state": "off"},
    {
        "id": 3,
        "label": "\u0412\u044b\u0445\u043e\u0434 7\u0433\u0440\u0435\u0445\u043e\u0432",
        "address": 57,
        "port": 2,
        "state": "off"
    },
    {
        "id": 4,
        "label": "\u0421\u0432\u0435\u0442 \u0442\u0435\u0430\u0442\u0440 \u0437\u0435\u0440\u043a\u0430\u043b\u043e",
        "address": 57,
        "port": 4,
        "state": "off"
    },
    {
        "id": 5,
        "label": "\u0421\u0446\u0435\u043d\u0430 \u0422\u0435\u0430\u0442\u0440 \u043d\u0438\u0448\u0430 ",
        "address": 57,
        "port": 1,
        "state": "off"
    },
    {
        "id": 6,
        "label": "\u0421\u0432\u0435\u0442 \u0442\u0435\u043c\u043d\u0430\u044f \u043a\u043e\u043c\u043d\u0430\u0442\u0430 - LED",
        "address": 57,
        "port": 3,
        "state": "off"
    }, {
        "id": 7,
        "label": "\u0442\u0435\u043c\u043d\u0430\u044f \u043a\u043e\u043c\u043d\u0430\u0442\u0430 - LED",
        "address": 58,
        "port": 3,
        "state": "off"
    }, {
        "id": 8,
        "label": "\u0421\u0432\u0435\u0442 \u041a\u043e\u0440\u0438\u0434\u043e\u0440  ",
        "address": 69,
        "port": 4,
        "state": "off"
    }, {
        "id": 9,
        "label": "\u0421\u0432\u0435\u0442 \u0422\u0451\u043c\u043d\u0430\u044f \u043a\u043e\u043c\u043d\u0430\u0442\u0430  ",
        "address": 69,
        "port": 3,
        "state": "off"
    }, {
        "id": 10,
        "label": "\u0421\u0432\u0435\u0442 \u041a\u043b\u0430\u0434\u0431\u0438\u0449\u0435  ",
        "address": 5,
        "port": 2,
        "state": "off"
    }, {"id": 11, "label": " \u0424\u0438\u043d\u0430\u043b ", "address": 61, "port": 0, "state": "off"}, {
        "id": 12,
        "label": "\u0420\u0435\u0441\u0442\u0430\u0440\u0442",
        "address": 58,
        "port": 4,
        "state": "off"
    }, {
        "id": 13,
        "label": " \u0434\u0432\u0435\u0440\u044c 1 -\u041a\u0440\u0430\u0441\u043d\u0430\u044f \u043a\u043e\u043c\u043d\u0430\u0442\u0430",
        "address": 61,
        "port": 7,
        "state": "off"
    }, {
        "id": 14,
        "label": " \u0434\u0432\u0435\u0440\u044c 2 -\u0422\u0435\u0430\u0442\u0440  ",
        "address": 61,
        "port": 1,
        "state": "off"
    }, {
        "id": 15,
        "label": " \u0434\u0432\u0435\u0440\u044c 3 -\u041a\u043b\u0430\u0434\u0431\u0438\u0449\u0435",
        "address": 61,
        "port": 6,
        "state": "off"
    }, {
        "id": 16,
        "label": " \u0434\u0432\u0435\u0440\u044c 4 -\u0422\u0451\u043c\u043d\u0430\u044f",
        "address": 61,
        "port": 2,
        "state": "off"
    }
];

const locksArray = [{
    "label": "\u0413\u043d\u0435\u0432",
    "address": 56,
    "port": 0,
    "puzzles": [{"reporter": "62:01:94:70:63:9d", "local_address": 8, "state": "not solved"}],
    "state": "closed"
}, {
    "label": "\u0423\u043d\u044b\u043d\u0438\u0435",
    "address": 56,
    "port": 1,
    "puzzles": [{"reporter": "a2:20:a6:02:08:b4", "local_address": 11, "state": "not solved"}],
    "state": "closed"
}, {
    "label": "\u0413\u043e\u0440\u0434\u044b\u043d\u044f - \u0441\u0432\u0435\u0442",
    "address": 56,
    "port": 2,
    "puzzles": [{"reporter": "5e:cf:7f:89:2a:9a", "local_address": 12, "state": "not solved"}],
    "state": "closed"
}, {
    "label": "\u0413\u043e\u0440\u0434\u044b\u043d\u044f - \u043a\u043e\u0434",
    "address": 56,
    "port": 3,
    "puzzles": [{"reporter": "5e:cf:7f:89:2a:9a", "local_address": 13, "state": "not solved"}],
    "state": "closed"
}, {
    "label": "\u0410\u043b\u0447\u043d\u043e\u0441\u0442\u044c",
    "address": 56,
    "port": 4,
    "puzzles": [{"reporter": "a2:20:a6:13:2d:80", "local_address": 14, "state": "not solved"}],
    "state": "closed"
}, {
    "label": "\u041e\u0431\u0436\u043e\u0440\u0441\u0442\u0432\u043e - \u043a\u043e\u043d\u0444\u0435\u0442\u044b",
    "address": 56,
    "port": 7,
    "puzzles": [{"reporter": "62:01:94:70:67:b3", "local_address": 21, "state": "not solved"}],
    "state": "closed"
}, {
    "label": "\u041e\u0431\u0436\u043e\u0440\u0441\u0442\u0432\u043e - \u0444\u0440\u0443\u043a\u0442\u044b",
    "address": 57,
    "port": 0,
    "puzzles": [{
        "reporter": "62:01:94:70:67:b3",
        "local_address": 22,
        "state": "not solved"
    }, {"reporter": "62:01:94:70:67:b3", "local_address": 23, "state": "not solved"}],
    "state": "closed"
}, {
    "label": "\u0421\u0446\u0435\u043d\u0430 \u041a\u041e\u0414",
    "address": 57,
    "port": 7,
    "puzzles": [{"reporter": "a2:20:a6:02:67:a9", "local_address": 25, "state": "not solved"}],
    "state": "closed"
}, {
    "label": "\u0417\u0435\u0440\u043a\u0430\u043b\u043e ",
    "address": 58,
    "port": 7,
    "puzzles": [{"reporter": "5e:cf:7f:1b:7a:e8", "local_address": 19, "state": "solved"}],
    "state": "open"
}, {
    "label": "\u0422\u0435\u0430\u0442\u0440 \u0412\u042b\u0425\u041e\u0414 ",
    "address": 57,
    "port": 6,
    "puzzles": [{"reporter": "a2:20:a6:12:2a:9b", "local_address": 24, "state": "not solved"}],
    "state": "closed"
}, {
    "label": "\u043e\u043e\u043e\u043e\u043e",
    "address": 57,
    "port": 4,
    "puzzles": [{"reporter": "5e:cf:7f:1b:7a:e8", "local_address": 19, "state": "solved"}],
    "state": "open"
}, {
    "label": "\u0442\u0435\u043c\u043d\u0430\u044f \u043a\u043e\u043c\u043d\u0430\u0442\u0430 \u0412\u042b\u0425\u041e\u0414",
    "address": 57,
    "port": 5,
    "puzzles": [{"reporter": "5e:cf:7f:1a:b6:2e", "local_address": 9, "state": "not solved"}],
    "state": "closed"
}, {
    "label": "\u041a\u0440\u0435\u0441\u0442",
    "address": 58,
    "port": 6,
    "puzzles": [{"reporter": "5e:cf:7f:87:56:5c", "local_address": 20, "state": "not solved"}],
    "state": "closed"
}, {
    "label": "\u0441\u0443\u043d\u0434\u0443\u043a 1",
    "address": 58,
    "port": 2,
    "puzzles": [{"reporter": "5e:cf:7f:87:56:52", "local_address": 15, "state": "not solved"}],
    "state": "closed"
}, {
    "label": "\u0441\u0443\u043d\u0434\u0443\u043a 2",
    "address": 58,
    "port": 5,
    "puzzles": [{"reporter": "5e:cf:7f:1a:ba:df", "local_address": 16, "state": "not solved"}],
    "state": "closed"
}, {
    "label": "\u0441\u0443\u043d\u0434\u0443\u043a 3",
    "address": 58,
    "port": 1,
    "puzzles": [{"reporter": "5e:cf:7f:1b:60:98", "local_address": 17, "state": "not solved"}],
    "state": "closed"
}, {
    "label": "\u0441\u0443\u043d\u0434\u0443\u043a 4",
    "address": 58,
    "port": 0,
    "puzzles": [{"reporter": "62:01:94:70:58:ed", "local_address": 18, "state": "not solved"}],
    "state": "closed"
}];
const locks = {
        fetch: () => Promise.resolve(locksArray)
};

const switches = {
        fetch: () => Promise.resolve(switchesArray),
set: (id, state) => {
    console.log(`[${id}] new state ${state}`);
    return Promise.resolve();
}
};

const puzzles = {
        set: (reporter, address, state) => {
        console.log(`[${reporter}:${address}] new state ${state}`);
        return Promise.resolve();
        }
};

const games = {
        fetch: () => Promise.resolve(27),
next: () =>{
    console.log('next game');
    return Promise.resolve();
}
};


export {
    switches,
    locks,
    games,
    puzzles
};