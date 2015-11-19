{
  'targets' : [
    {
      'target_name' : 'glew-static',
      'type' : 'static_library',
      'sources' : [
        'deps/glew/src/glew.c'
      ],
      'defines': [
        'GLEW_STATIC'
      ],
      'include_dirs' : [
        'deps/glew/include'
      ]
    }
  ]
}
