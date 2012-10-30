Blog::Application.routes.draw do
  resources :todos do
    member do
      get :finished
    end
  end

  root :to => "todos#index"
end
