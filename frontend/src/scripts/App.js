import '../scss/App.scss';
import React from 'react';

function App(props) {
  const { user } = props;

  return (
    <div>
      {/* {user.is_authenticated ? (
        <div>
          Hello <b>{user.username}</b> - you can logout{' '}
          <a href="/logout">here</a>
        </div> 
      ) : (*/}
        <div>
          <a href="/register">You can register here</a> <br />
          <a href="/login">You can login here</a>
        </div>
      {/* )} */}

      <br />

      <div>
        Here's the full list of apps I've created:
        <ul>
          <li>
            <a href="seotool">
              <b>Simple SEO tool</b>
            </a>
            <br />
            <i>Multiple external RestAPI usage</i>
          </li>
          <li>
            <a href="quotes">
              <b>Quotes generator</b>
            </a>
            <br />
            <i>External RestAPI usage - GET / POST</i>
          </li>
          <li>
            <a href="to-do-list">
              <b>To do list</b>
            </a>
            <br />
            <i>Simple CRUD</i>
          </li>
        </ul>
      </div>
    </div>
  );
}

export default App;
